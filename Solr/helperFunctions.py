import re
from collections import OrderedDict

def underscore2dot(string):
    return re.sub('_', '.', string)

def correctSolrKeywords(dictionary):
    """ transform _ into . in dictionary keywords so you can 
        use facet_field as a keyword for the _get_search_params method.
        Note that python doesn't allow for dots in keyword argument names"""
    return {underscore2dot(key): value
               for key, value in dictionary.iteritems()}

def getDesiredDictTreeLevel(dictTree, level = 'root'):
    if level == 'root':
        return dictTree
    else:
        currentLevel = dictTree
        for entry in level.split('.'):
            currentLevel = currentLevel.get(entry, currentLevel)
        return currentLevel

def dictionaryFromFacetDataList(facetDataList):
    fieldValues = facetDataList[::2]
    fieldCounts = facetDataList[1::2]
    return OrderedDict(zip(fieldValues, fieldCounts))
