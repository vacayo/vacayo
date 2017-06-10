from django.views.generic.edit import View
from django.http import JsonResponse
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA2Oc07uU1kr_vkiJ_lWQ6xF7nT6pS9RNg')

class AddressView(View):
    template_name = 'address.html'

    def get(self, request):
        address = request.GET.get('query')
        geocode_result = gmaps.geocode(address)

        if not address:
            raise Exception('No address provided')

        # print(geocode_result)
        results = [result['formatted_address'] for result in geocode_result if 'formatted_address' in result]

        return JsonResponse({
            'status': 'ok',
            'results': results
        })
