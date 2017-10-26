import geopy
import usaddress
import googlemaps
from django.conf import settings
from django.utils.dateparse import parse_datetime
from django.db.models import F
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from ..apis.zillow import ZillowAPI
from ..models import Zip, Property, Host


class PropertyService(object):

    def __init__(self):
        self.zillow = ZillowAPI()
        self.gmaps = googlemaps.Client(settings.GOOGLE_API_KEY)

    def create(self, address, bedrooms, bathrooms, home_type, home_size, available_date, last_rent, offer, *args, **kwargs):
        lat, lng = self.geolocate(address)
        address = self.parse(address)
        available_date = parse_datetime(available_date).date()

        property, _ = Property.objects.get_or_create(
            address1=address.get('address1'),


            address2=address.get('address2'),
            city=address.get('city'),
            state=address.get('state'),
            zip_code=address.get('zip_code'),
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            home_type=home_type,
            home_size=home_size,
            available_date=available_date,
            last_rent=last_rent,
            offer=offer,
            latitude=lat,
            longitude=lng
        )

        return property

    def lookup(self, address):
        pass

    def geocode(self, address):
        result = self.gmaps.geocode(address)

        return [{
            'address': _['formatted_address'],
            'latitude': _['geometry']['location']['lat'],
            'longitude': _['geometry']['location']['lng'],
        } for _ in result if 'formatted_address' in _]

    def geolocate(self, address):
        geolocator = geopy.geocoders.GoogleV3(api_key=settings.GOOGLE_API_KEY)
        location = geolocator.geocode(address)
        return location.latitude, location.longitude

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

    def meta(self, address):
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

        # Lookup the property against Zillow
        result = self.zillow.lookup(address1, citystatezip)
        # print "Address:", result.street, result.city, result.state, result.zipcode
        # print "Low:", result.rentzestimate_range_low
        # print "Hight:", result.rentzestimate_range_high

        # Determine if this property is in our service range
        in_service = Zip.objects.filter(code=result.zipcode, in_service=True).exists()

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
            'in_service': in_service
        }

    def assign_owner(self, property, owner):
        property.owners.add(owner)

    def assign_host(self, property, host=None):
        # a host was provided so just assign
        if host:
            property.hosts.add(host)
            return

        # geolocate the property
        lat, lng = self.geolocate(property.address)
        geo = Point(lat, lng, srid=4326)

        # attempt to find the closest host that is within range
        if not host:
            host = Host.objects.annotate(distance=Distance('geo', geo)).filter(active=True, distance__lte=F('radius') * 1609.34).order_by('-distance').first()
            property.hosts.add(host)
            return

        # attempt to find the closest host regardless if within range
        if not host:
            host = Host.objects.annotate(distance=Distance('geo', geo)).filter(active=True).order_by('-distance').first()
            print "Closest host is {}, would you like to assign?".format(host)
            return
