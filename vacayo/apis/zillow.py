from pyzillow.pyzillow import ZillowWrapper, ZillowResults
from pyzillow.pyzillowerrors import ZillowError, ZillowFail, ZillowNoResults

class ZillowAPI(object):

    def __init__(self):
        self.zillow = ZillowWrapper('X1-ZWz1fuwo60hszv_6msnx')

    def lookup(self, address, citystatezip):
        try:
            return self.ZillowPropertyResults(
                self.zillow.get_data(
                    'http://www.zillow.com/webservice/GetDeepSearchResults.htm',
                    {
                        'address': address,
                        'citystatezip': citystatezip,
                        'zws-id': self.zillow.api_key,
                        'rentzestimate': True
                    }
                )
            )
        except (ZillowError, ZillowFail, ZillowNoResults), e:
            return []

    class ZillowPropertyResults(ZillowResults):
        attribute_mapping = {
            'zillow_id': 'result/zpid',
            'home_type': 'result/useCode',
            'home_detail_link': 'result/links/homedetails',
            'graph_data_link': 'result/links/graphsanddata',
            'map_this_home_link': 'result/links/mapthishome',
            'latitude': 'result/address/latitude',
            'longitude': 'result/address/longitude',
            'tax_year': 'result/taxAssessmentYear',
            'tax_value': 'result/taxAssessment',
            'year_built': 'result/yearBuilt',
            'property_size': 'result/lotSizeSqFt',
            'home_size': 'result/finishedSqFt',
            'bathrooms': 'result/bathrooms',
            'bedrooms': 'result/bedrooms',
            'last_sold_date': 'result/lastSoldDate',
            'last_sold_price': 'result/lastSoldPrice',

            # Zestimate
            'zestimate_amount': 'result/zestimate/amount',
            'zestimate_last_updated': 'result/zestimate/last-updated',
            'zestimate_value_change': 'result/zestimate/valueChange',
            'zestimate_valuation_range_high': 'result/zestimate/valuationRange/high',
            'zestimate_valuationRange_low': 'result/zestimate/valuationRange/low',
            'zestimate_percentile': 'result/zestimate/percentile',

            # Rent Zestimate
            'rentzestimate_amount': 'result/rentzestimate/amount',
            'rentzestimate_last_updated': 'result/rentzestimate/last-updated',
            'rentzestimate_value_change': 'result/rentzestimate/valueChange',
            'rentzestimate_valuation_range_high': 'result/rentzestimate/valuationRange/high',
            'rentzestimate_valuationRange_low': 'result/rentzestimate/valuationRange/low',

            # Address
            'street': 'result/address/street',
            'zipcode': 'result/address/zipcode',
            'city': 'result/address/city',
            'state': 'result/address/state',
        }

        def __init__(self, data, *args, **kwargs):
            """
            Creates instance of GeocoderResult from the provided XML data array
            """

            # from xml.etree import ElementTree
            # from xml.dom import minidom
            # print(minidom.parseString(ElementTree.tostring(data, encoding='utf8', method='xml')).toprettyxml())

            self.data = data.findall('response/results')[0]
            for attr in self.attribute_mapping.__iter__():
                try:
                    self.__setattr__(attr, self.get_attr(attr))
                except AttributeError:
                    print ('AttributeError with %s' % attr)
