import json
from django.views.generic.edit import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..services.property import PropertyService

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

        return JsonResponse({
            'status': 'ok'
        })
