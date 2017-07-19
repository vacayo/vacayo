from ..apis.zillow import ZillowAPI
import usaddress
import googlemaps


class PropertyService(object):

    def __init__(self):
        self.zillow = ZillowAPI()
        self.gmaps = googlemaps.Client('AIzaSyA2Oc07uU1kr_vkiJ_lWQ6xF7nT6pS9RNg')

    def geocode(self, address):
        result = self.gmaps.geocode(address)

        return [_['formatted_address'] for _ in result if 'formatted_address' in _]

    def parse(self, address):
        address, address_type = usaddress.tag(address, tag_mapping={
            'Recipient': 'recipient',
            'AddressNumber': 'address1',
            'AddressNumberPrefix': 'address1',
            'AddressNumberSuffix': 'address1',
            'StreetName': 'address1',
            'StreetNamePreDirectional': 'address1',
            'StreetNamePreModifier': 'address1',
            'StreetNamePreType': 'address1',
            'StreetNamePostDirectional': 'address1',
            'StreetNamePostModifier': 'address1',
            'StreetNamePostType': 'address1',
            'CornerOf': 'address1',
            'IntersectionSeparator': 'address1',
            'LandmarkName': 'address1',
            'USPSBoxGroupID': 'address1',
            'USPSBoxGroupType': 'address1',
            'USPSBoxID': 'address1',
            'USPSBoxType': 'address1',
            'OccupancyType': 'address1',
            'OccupancyIdentifier': 'address1',
            'SubaddressIdentifier': 'address1',
            'SubaddressType': 'address1',
            'BuildingName': 'address2',
            'PlaceName': 'city',
            'StateName': 'state',
            'ZipCode': 'zip_code',
            'CountryName': 'country'
        })

        return address

    def lookup(self, address):
        # address1 = '4117 Crescent St APT 7F'
        # citystatezip = 'Long Island City, NY 11101'
        # result = self.zillow.lookup(address1, citystatezip)

        address = self.parse(address)
        address1 = address.get('address1')
        citystatezip = '{} {} {}'.format(
            address.get('city', ''),
            address.get('state', ''),
            address.get('zip_code', '')
        ).strip()

        result = self.zillow.lookup(address1, citystatezip)

        # print "Address:", result.street, result.city, result.state, result.zipcode
        # print "Low:", result.rentzestimate_range_low
        # print "Hight:", result.rentzestimate_range_high

        return {
            'home_type': result.home_type,
            'year_built': result.year_built,
            'property_size': result.property_size,
            'home_size': result.home_size,
            'bathrooms': float(result.bathrooms or 1),
            'bedrooms': int(result.bedrooms or 1),
            'value_estimate': result.zestimate_amount,
            'rent_estimate': result.rentzestimate_amount,
            'rent_estimate_low': result.rentzestimate_range_low,
            'rent_estimate_high': result.rentzestimate_range_high,
        }
