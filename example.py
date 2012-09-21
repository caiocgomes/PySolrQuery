from Solr import Solr

class MySolr(Solr):
    def _basic_fixed_params(self):
        base = Solr._basic_fixed_params(self)
        base.update({'qt': 'matchName'})
        return base

    def _required_params(self):
        base = Solr._required_params(self)
        base.append('fl')
        return base

if __name__ == '__main__':
    solr = MySolr(host='192.168.1.30', port = '8088', appName = 'content', coreName='local')
    # simple query example
    searchResult = solr.doSearch(q = 'pizza', fl = 'name, city', rows=20)
    for i, item in enumerate(searchResult):
        print i, item

    # facet example
    facetResult = solr.doFacet(q = 'pizza', field = 'city', fl = '')
    for value, count in facetResult.iteritems():
        if count > 300:
            print value, count

