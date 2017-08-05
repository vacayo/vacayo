"""vacayo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from vacayo.views.api import AddressView, PropertyView, PropertiesView, RegistrationView


class StaticPageView(TemplateView):
    context = None

    def get_context_data(self, **kwargs):
        context = super(StaticPageView, self).get_context_data(**kwargs)
        context.update(self.context or {})
        return context


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='wp.html'), name='home'),
    url(r'^register', StaticPageView.as_view(template_name='vue.html', context={'vue': 'registration'}), name='registration'),
    url(r'^dashboard', login_required(StaticPageView.as_view(template_name='vue2.html', context={'vue': 'dashboard'})), name='dashboard'),

    url(r'api/address', AddressView.as_view()),
    url(r'api/property', PropertyView.as_view()),
    url(r'api/properties', PropertiesView.as_view()),
    url(r'api/registration', RegistrationView.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', TemplateView.as_view(template_name='account/account_profile.html'), name='account_profile'),
    url(r'^accounts/update/(?P<username>[\w-]+)', TemplateView.as_view(template_name='account/account_update.html'), name='account_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
