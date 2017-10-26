from django.core.management.base import BaseCommand, CommandError
from ...services.property import PropertyService
from ...models.property import Property
from pprint import pprint

property_service = PropertyService()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        address = options['address']

        pprint(property_service.geocode(address))

        pprint(property_service.meta(address))

        pprint(property_service.geolocate(address))
