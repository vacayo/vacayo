from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class Redirect404Middleware(MiddlewareMixin):

    def process_response(self, request, response):

        if isinstance(response, HttpResponseNotFound):
            return HttpResponseRedirect('http://homes.vacayo.com/%s' % (request.path,))

        return response
