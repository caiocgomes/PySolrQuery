import requests
import re
from helperFunctions import *
from SolrExceptions import *

class Solr(object):
    def __init__(self, host = 'mySolrHost', port = 8088, appName = '', coreName = ''):
        self.hosturl = self._get_base_url(host, port, appName, coreName)

    def _get_base_url(self, host, port, appName, coreName):
        return 'http://{host}:{port}/{appName}/{coreName}/select/'.format(**locals())

    def _make_request(self, data = {}):
        req = requests.post(self.hosturl, data = data)
        return eval(req.content)

    def _basic_fixed_params(self):
        return {'wt': 'python'}

    def _required_params(self):
        return ["q"]

    def _get_search_params(self, pars = {}, **kwargs):
        base = self._basic_fixed_params()
        base.update(pars)
        base.update(correctSolrKeywords(kwargs))
        return base

    def _check_for_missing_required_parameters(self, passedPars):
        requiredPars = self._required_params()
        missingPars = [par for par in requiredPars if par not in passedPars]
        if len(missingPars) > 0:
            raise RequiredParamException(missingPars)

    def getSearchData(self, pars = {}, **kwargs):
        data = self._get_search_params(pars = pars, **kwargs)
        passedParList = data.keys()
        self._check_for_missing_required_parameters(passedParList)
        return data

    def doSearch(self, **kwargs):
        data = self.getSearchData(**kwargs)
        resp = self._make_request(data = data)
        return getDesiredDictTreeLevel(resp, level = 'response.docs')

    def doFacet(self, field, mincount = 1, **kwargs):
        additionalFacetParameters = {'facet': 'true', 'facet.field': field, 'rows': 0, 'facet.mincount': mincount}
        data = self.getSearchData(pars = additionalFacetParameters, **kwargs)
        resp = self._make_request(data = data)
        facetDataList = getDesiredDictTreeLevel(resp, level = 'facet_counts.facet_fields.{field}'.format(**locals()))
        return dictionaryFromFacetDataList(facetDataList)





