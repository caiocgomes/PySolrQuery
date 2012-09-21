PySolrQuery
===========

A tentative API for interacting with Solr from python.

What is PySolrQuery?
--------------------

PySolrQuery is a lightweight module to do Solr searches within python.

How do I use it?
----------------

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

You can pass query parameters as keyword arguments:

```python
> searchResults = solr.doSearch(q = 'name:Mary', fl = 'name, profession, age', fq = 'age)
```

You can easily create custom searches by extending the Solr class:

```python
class MyCustomSearch(Solr)
    def _basic_fixed_params(self):
        base = Solr._basic_fixed_params(self)
        return base + {'defType': 'dismax', 'qf': 'name^2.0 parentsname^1.0 profession^0.5'}


solr = MyCustomSearch(host = 'localhost')
print solr.doSearch(q = 'mary doctor')
```

Parameters returned by the ```Solr._basic_fixed_params()``` method are made fixed over all queries and parameters returned by the ```Solr._required_params()``` method raise a RequiredParamException when not present in a call to doSearch() or doFacet().
