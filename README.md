Open Semantic Visual Linked Data Knowledge Graph Explorer
=========================================================


Open Source web app and user interace (UI) for discovery, exploration and visualization of a graph
--------------------------------------------------------------------------------------------------

Open Semantic Visual Linked Data Knowledge Graph Explorer is a web app providing user interfaces (UI) to discover, explore and visualize linked data in a graph for visualization and exploration of direct and indirect connections between entities like people, organizations and locations in your Linked Data Knowledge Graph (for example extracted from your documents by Open Semantic Search or Open Semantic ETL).


Visual graph user interfaces (UI)
---------------------------------

Learn more about usage of the graph user interfaces in the documentation (including screenshots):

https://opensemanticsearch.org/doc/analytics/graph


Document & thesaurus based entity graph exploration by co-occurrences of entities in documents
----------------------------------------------------------------------------------------------

A click on a connection / edge with the connection type / property "Documents (co-occurrence)" shows you in how many and which documents the connected entities occur together.

In the tab "List" you see a list of documents in which both connected entities occur.

In the tab "Preview" you can preview the single documents.

In the tab "Entities" or other options in the sub menu "Analyze" you can analyze & filter this documents and other named entities within this documents.

If you set up a thesaurus or an ontology, the linked concepts of your thesaurus or the selected ontology are shown in the graph, too, so additionally to occuring entities you can explore by concepts of your thesaurus or ontologies in the document content, too.


Architecture: Integrates Python Django, Apache Solr and Cytoscape.js
--------------------------------------------------------------------

The Django web app for discovery, exploration and visualization of a graph integrates a Neo4j graph database (planed) with documents in a Apache Solr search index with the Cytoscape.js graph visualization framework.


Dependencies
------------

If you do not want to use the preconfigured Debian or Ubuntu packages, you have to setup the following dependencies:

- Python 3 (https://www.python.org/)
- Django (https://www.djangoproject.com/)
- cytoscape.js (Git: https://github.com/cytoscape/cytoscape.js)
- cytoscape.js-panzoom (Git: https://github.com/cytoscape/cytoscape.js-panzoom)
- Foundation (https://foundation.zurb.com/)


Optional dependencies / integration
-----------------------------------

Optional dependencies for integrated graph database(s) or faceted search index where your knowledge graph, entities, connections and/or documents are stored:

- Apache Solr (https://lucene.apache.org/solr/)
- Planned: Neo4j (https://neo4j.com)
- Planned: SPARQL triplestore like Apache Jena (https://jena.apache.org/)
