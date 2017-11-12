import json
import pytz
import datetime

from django.utils.decorators import method_decorator
from django.views.generic.edit import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from django.utils import timezone

from ..services.notification import NotificationService
from ..services.property import PropertyService
from ..services.user import UserService
from ..models import Host, Property

property_service = PropertyService()
user_service = UserService()


# PROPERTY REGISTRATION #

@method_decorator(csrf_exempt, name='dispatch')
class AddressView(View):

    def get(self, request):
        address = request.GET.get('query')

        if not address:
            raise Exception('No address provided')

        addresses = property_service.geocode(address)

        return JsonResponse({
            'status': 'ok',
            'results': addresses
        })


@method_decorator(csrf_exempt, name='dispatch')
class PropertyView(View):

    def get(self, request):
        address = request.GET.get('address')

        if not address:
            raise Exception('No address provided')

        prop = property_service.meta(address)

        return JsonResponse({
            'status': 'ok',
            'results': prop
        })


@method_decorator(csrf_exempt, name='dispatch')
class RegistrationView(View):

    def post(self, request):
        data = json.loads(request.body)
        owner_data = data.get('owner')
        property_data = data.get('property')

        with transaction.atomic():
            # Create User, Owner and Property Record
            user = user_service.create(**owner_data)
            property = property_service.create(**property_data)

            # Assign Owner and Host
            owner = user_service.assign_owner_role(user, **owner_data)
            property_service.assign_owner(property, owner)
            property_service.assign_host(property)

            # Send notifications
            NotificationService.send_new_property_notifications(property)

        return JsonResponse({
            'status': 'ok'
        })


@method_decorator(csrf_exempt, name='dispatch')
class LeadView(View):

    def post(self, request):
        data = json.loads(request.body)
        owner_data = data.get('owner')
        property_data = data.get('property')

        with transaction.atomic():
            # Create Lead record
            lead = user_service.record_lead(property_data.get('address'), **owner_data)

            # Send notifications
            NotificationService.send_new_lead_notifications(lead)

        return JsonResponse({
            'status': 'ok'
        })


# DASHBOARD #

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        host = Host.objects.filter(user=user).first()

        return JsonResponse({
            'status': 'ok',
            'results': {
                'user': {
                    'first_name': user.get_short_name(),
                    'last_name': user.last_name,
                    'full_name': user.get_full_name(),
                    'host': host.to_dict() if host else None
                } if user else None
            }
        })

    def post(self, request):
        data = json.loads(request.body)
        user_data = data.get('user')

        with transaction.atomic():
            user = user_service.create(**user_data)
            user_service.login(request, user.email, user_data.get('password1'))

        return JsonResponse({
            'status': 'ok',
            'results': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }
        })

    @method_decorator(login_required)
    def patch(self, request):
        user = request.user
        data = json.loads(request.body)

        user.first_name = data['first_name']
        user.last_name = data['last_name']

        user.save()

        return JsonResponse({
            'status': 'ok'
        })


@method_decorator(csrf_exempt, name='dispatch')
class HostView(View):

    @method_decorator(login_required)
    def post(self, request):
        data = json.loads(request.body)
        accepted_agreement_on = data.get('accepted_agreement_on')

        host = user_service.assign_host_role(request.user)
        host.accepted_agreement_on = timezone.now()
        host.save()

        return JsonResponse({
            'status': 'ok'
        })

    @method_decorator(login_required)
    def patch(self, request):
        host = Host.objects.get(user=request.user)
        data = json.loads(request.body)
        active = data.get('active')
        radius = data.get('radius')
        location = data.get('location')

        host.active = active
        host.radius = radius
        host.save()

        host.location.address = location['address']
        host.location.latitude = location['latitude']
        host.location.longitude = location['longitude']
        host.location.save()

        return JsonResponse({
            'status': 'ok',
            'results': host.to_dict()
        })


@method_decorator(csrf_exempt, name='dispatch')
class PropertiesView(View):

    @method_decorator(login_required)
    def get(self, request):
        owned_properties = {
            p.id: {
                'id': p.id,
                'offer': p.offer,
                'status': p.status,
                'location': p.location.to_dict(),
                'bedrooms': p.bedrooms,
                'bathrooms': p.bathrooms,
                'visit_date': p.visit_date.strftime('%m/%d/%Y') if p.visit_date else None,
                'main_image': p.main_image.url if p.main_image else None,
                'onboarding_statuses': p.onboarding_statuses,
                'relationship': 'OWNED'
            } for p in Property.objects.filter(owners__user__email=request.user.email)
        }

        hosted_properties = {
            p.id: {
                'id': p.id,
                'offer': p.offer,
                'status': p.status,
                'location': p.location.to_dict(),
                'bedrooms': p.bedrooms,
                'bathrooms': p.bathrooms,
                'visit_date': p.visit_date.strftime('%m/%d/%Y') if p.visit_date else None,
                'main_image': p.main_image.url if p.main_image else None,
                'onboarding_statuses': p.onboarding_statuses,
                'relationship': 'HOSTED'
            } for p in Property.objects.filter(hosts__user=request.user)
        }

        return JsonResponse({
            'status': 'ok',
            'results': dict(owned_properties.items() + hosted_properties.items())
        })

    @method_decorator(login_required)
    def post(self, request):
        data = json.loads(request.body)
        p = Property.objects.get(pk=data.get('id'))
        p.visit_date = pytz.utc.localize(datetime.datetime.strptime(data.get('visit_date'), '%m/%d/%Y'))
        p.save()

        return JsonResponse({
            'status': 'ok',
            'results': {
                'id': p.id,
                'offer': p.offer,
                'status': p.status,
                'location': p.location.to_dict(),
                'bedrooms': p.bedrooms,
                'bathrooms': p.bathrooms,
                'visit_date': p.visit_date.strftime('%m/%d/%Y') if p.visit_date else None,
                'main_image': p.main_image.url if p.main_image else None,
                'onboarding_statuses': p.onboarding_statuses
            }
        })
