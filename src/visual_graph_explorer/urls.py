from django.conf.urls import url

from visual_graph_explorer import views

urlpatterns = [
	url(r'^$', views.graph, name='graph'),
	url(r'^graph', views.graph, name='graph'),
	url(r'^select', views.select, name='select'),
]
