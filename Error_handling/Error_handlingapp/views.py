# error_handling_app/views.py

from django.shortcuts import render
from django.http import HttpResponseNotFound

def successful(request):
    return HttpResponseNotFound('Successful', status=200)

def created(request):
    return HttpResponseNotFound('Created', status=201)

def accepted(request):
    return HttpResponseNotFound('Accepted', status=202)

def non_authorization_info(request):
    return HttpResponseNotFound('Non-Authoritative Information', status=203)

def found(request):
    return HttpResponseNotFound('Found', status=302)

def bad_request(request):
    return HttpResponseNotFound('Bad Request', status=400)

def unauthorized(request):
    return HttpResponseNotFound('Unauthorized', status=401)

def payment_required(request):
    return HttpResponseNotFound('Payment Required', status=402)

def forbidden(request):
    return HttpResponseNotFound('Forbidden', status=403)

# def not_found(request):
#     return HttpResponseNotFound('Not Found', status=404)

def request_timeout(request):
    return HttpResponseNotFound('Request Timeout', status=408)

def conflict(request):
    return HttpResponseNotFound('Conflict', status=409)

def uri_too_long(request):
    return HttpResponseNotFound('URI Too Long', status=414)

def internal_server_error(request):
    return HttpResponseNotFound('Internal Server Error', status=500)

def bad_gateway(request):
    return HttpResponseNotFound('Bad Gateway', status=502)

def service_unavailable(request):
    return HttpResponseNotFound('Service Unavailable', status=503)

def http_version_not_supported(request):
    return HttpResponseNotFound('HTTP Version Not Supported', status=505)

def network_authentication_required(request):
    return HttpResponseNotFound('Network Authentication Required', status=511)

def loop_detected(request):
    return HttpResponseNotFound('Loop Detected', status=508)


def custom_404(request):
    return render(request, 'index.html')
