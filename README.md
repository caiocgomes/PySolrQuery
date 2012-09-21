PySolrQuery
===========

A tentative lightweight API for to make Solr queries within python.

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

Constructor parameters and Solr host URL:
-----------------------------------------

The constructor assumes that the path to your Solr core is: ```{host}:{port}/{appName}/{coreName}/select/```, 
where the values of  ```host```,```port```,```appName``` and ```coreName``` must be passed to the ```Solr``` constructor.

If this is not your case, check the method ```Solr._get_base_url()```. It must return the correct URL.

Query parameters as keyword arguments:
--------------------------------------

You can pass query parameters as keyword arguments:

```python
> searchResults = solr.doSearch(q = 'name:Mary', fl = 'name, profession, age', fq = 'age)
```

Python doesn't accept keyword arguments with dot '.' in its name. In this case, just substitute de dot by an underscore '_':

```python
> facetResult = solr.doFacet(q = 'name:Mary', field = 'profession', facet_mincount = 10)
```


Extending the Solr class:
-------------------------

You can easily create custom searches by extending the Solr class:

```python
class MyCustomSearch(Solr)
    def _basic_fixed_params(self):
        base = Solr._basic_fixed_params(self)
        return base + {'defType': 'dismax', 'qf': 'name^2.0 parentsname^1.0 profession^0.5'}


solr = MyCustomSearch(host = 'localhost')
print solr.doSearch(q = 'mary doctor')
```

Parameters returned by the ```Solr._basic_fixed_params()``` method are made fixed over all queries and parameters 
returned by the ```Solr._required_params()``` method raise a ```RequiredParamException``` when not present in a call 
to ```doSearch()``` or ```doFacet()```.

To do list and Known issues:
----------------------------

- needs a proper module structure
- needs a setup.py to deal with dependencies
- needs a better way to deal with the paths in the host URL.
- needs a way to do facets in multiple fields in the same query
- needs tests

Known issues:

- It's not possible to do multiple facets in the same query right now. This stems from the use of the ```requests``` module.
Query parameters are passed through a dictionary to the post method, and python dictionaries can't have two fields with the same key.

Dependencies:
-------------
- [requests](http://docs.python-requests.org/en/latest/index.html): just install it via ```sudo pip install requests```


