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

    def lookup(self, address):
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
            'PlaceName': 'citystatezip',
            'StateName': 'citystatezip',
            'ZipCode': 'citystatezip',
            'CountryName': 'country'
        })

        # address1 = '4117 Crescent St APT 7F'
        # citystatezip = 'Long Island City, NY 11101'
        # result = self.zillow.lookup(address1, citystatezip)

        result = self.zillow.lookup(address.get('address1'), address.get('citystatezip'))

        return {
            'home_type': result.home_type,
            'year_built': result.year_built,
            'property_size': result.property_size,
            'home_size': result.home_size,
            'bathrooms': float(result.bathrooms or 0),
            'bedrooms': int(result.bedrooms or 0),
            'zestimate_amount': result.zestimate_amount,
            'zestimate_last_updated': result.zestimate_last_updated,
            'rentzestimate_amount': result.rentzestimate_amount,
            'rentzestimate_last_updated': result.rentzestimate_last_updated,
            'home_detail_link': result.home_detail_link
        }
