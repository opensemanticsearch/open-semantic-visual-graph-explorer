# Open Semantic Visual Graph Explorer

from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
import django.utils.html
import requests
import json
import math

from thesaurus.models import Facet

solr='http://localhost:8983/solr/'
solr_core='opensemanticsearch'

size_min = 15
size_max = 100



def scale_weight(weight=1):
	if weight < size_min:
		weight = size_min
	if weight > size_max:
		weight = size_max

	return weight


def query( q="", limit=None):

	fields = []
	for facet in Facet.objects.filter(graph_enabled=True).order_by('facet_order'):
		fields.append(facet.facet)
		
	nodes = []
	edges = []

	if not limit:
		limit = -1

	headers = {'content-type' : 'application/json'}

	params = {
		'wt': 'json',
		'rows': 0, # we do not need document field results, only the facet
		'facet.limit': limit, # This param indicates the maximum number of constraint counts that should be returned for the facet fields. A negative value means unlimited.
		'facet.mincount': 1,
		'facet': 'on',
		'facet.field': fields,
		'q': q,
		'q.op': "AND"
	}
	
	r = requests.get(solr + solr_core + '/select', params=params, headers=headers)
	result = r.json()
	
	query_is_entity = False
		
	for facet in result['facet_counts']['facet_fields']:		
		
		is_value = True
		for value in result['facet_counts']['facet_fields'][facet]:
			if is_value:
				name = value
				id = value

				# next list entry is count
				is_value=False
			else:
				count = value
				
				if name == q.strip("\""):
					query_is_entitiy = True 
				nodes.append( {'data': {'id': id, 'name': name, 'weight': scale_weight(count), 'type': facet} })
				
				# next list entry is a value
				is_value = True

	if q:

		for node in nodes:
			
			edges.append( {'data': { 'source': q, 'target': node['data']['id'], 'weight': math.ceil(node['data']['weight']/2) } })

		if not query_is_entity:
			name = "Search for {}".format(q)
			nodes.append( {'data': {'id': q.strip("\""), 'name': name, 'weight': scale_weight(result['response']['numFound']), 'type': 'query'} })
	
	results = { 'nodes': nodes, 'edges': edges }

	return results

	
def graph(request):

	# query
	q = "*:*"
	limit = 100
	if request.GET:
		if 'q' in request.GET:
			q = request.GET['q']
		if 'limit' in request.GET:
			limit = int(request.GET['limit'])

	elements = query(q, limit=limit)


	# get facet layout
	facets={}

	for facet in Facet.objects.filter(graph_enabled=True).order_by('facet_order'):
		count = 0
		for node in elements['nodes']:
			if node['data']['type'] == facet.facet:
				count += 1
		facets[facet.facet]= {'label': facet.label, 'bg': facet.style_color_background, 'count': count}

	
	return render(request, 'graph.html', 
				{	
					"elements": django.utils.html.mark_safe(json.dumps(elements)),
					"facets": django.utils.html.mark_safe(json.dumps(facets)),
				})


def select(request):

	q = request.GET['q']

	limit = None
	if 'limit' in request.GET:
		limit = int(request.GET['limit'])

	results = query(q=q, limit=limit)
	
	return JsonResponse(results)
