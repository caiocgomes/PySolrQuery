PySolrQuery
===========

A tentative API for interacting with Solr from python.

- What is PySolrQuery?

PySolrQuery is a lightweight module to do Solr searches within python.

- How do I use it?

There's a Solr class with handy methods.

```python

> from Solr import Solr
> solr = Solr(host = 'localhost', appName = 'content', coreName = 'people')
> searchResults = solr.doSearch(q = 'name:John')

> for people in searchResults:
>     print people

{'name': 'John Lennon', 'profession': 'musician'}
{'name': 'John Wayne', 'profession': 'actor'}

> facetResults = solr.doFacet(q = 'name:John', field = 'profession')
> for profession, count in facetResults.iteritems():
>     print profession, count

musician 1
actor 1
```

