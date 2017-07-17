import json
from django.utils.dateparse import parse_datetime
from django.views.generic.edit import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..services.property import PropertyService
from ..models.owner import Owner
from ..models.property import Property

property_service = PropertyService()


class AddressView(View):

    def get(self, request):
        address = request.GET.get('query')

        if not address:
            raise Exception('No address provided')

        addresses = property_service.geocode(address)

        print(len(addresses))

        return JsonResponse({
            'status': 'ok',
            'results': [{'value': v} for v in addresses]
        })


class PropertyView(View):

    def get(self, request):
        address = request.GET.get('address')

        if not address:
            raise Exception('No address provided')

        prop = property_service.lookup(address)

        return JsonResponse({
            'status': 'ok',
            'results': prop
        })


@method_decorator(csrf_exempt, name='dispatch')
class RegistrationView(View):

    def post(self, request):
        data = json.loads(request.body)
        
        owner, _ = Owner.objects.get_or_create(
            first_name=data.get('first_name'), 
            last_name=data.get('last_name'), 
            email=data.get('email'),
            phone=data.get('phone')
        )

        address = property_service.parse(data.get('address'))
        property, _ = Property.objects.get_or_create(
            address1=address.get('address1'),
            address2=address.get('address2'),
            city=address.get('city'),
            state=address.get('state'),
            zip_code=address.get('zip_code'),
            bedrooms=data.get('bedrooms'),
            bathrooms=data.get('bathrooms'),
            home_type=data.get('home_type'),
            home_size=data.get('home_size'),
            available_date=parse_datetime(data.get('available_date')).date(),
            last_rent=data.get('last_rent'),
        )

        owner.properties.add(property)

        return JsonResponse({
            'status': 'ok'
        })
