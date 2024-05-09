# error_handling_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('successful/', views.successful),
    path('created/', views.created),
    path('accepted/', views.accepted),
    path('non-authorization-info/', views.non_authorization_info),
    path('found/', views.found),
    path('bad-request/', views.bad_request),
    path('unauthorized/', views.unauthorized),
    path('payment-required/', views.payment_required),
    path('forbidden/', views.forbidden),
    # path('not-found/', views.not_found),
    path('request-timeout/', views.request_timeout),
    path('conflict/', views.conflict),
    path('uri-too-long/', views.uri_too_long),
    path('internal-server-error/', views.internal_server_error),
    path('bad-gateway/', views.bad_gateway),
    path('service-unavailable/', views.service_unavailable),
    path('http-version-not-supported/', views.http_version_not_supported),
    path('network-authentication-required/', views.network_authentication_required),
    path('loop-detected/', views.loop_detected),
]
