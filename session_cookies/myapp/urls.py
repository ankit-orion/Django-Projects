from django.urls import path
from .import views
urlpatterns = [
    path('set-cookies/', views.set_cookies, name='set_cookies'),
    path('get-cookies/',views.get_cookies, name='get-cookies'),
    path('delete-cookies/', views.delete_cookies, name='delete-cookis'),
    path('set-session/', views.set_session, name='set-session'),
    path('get-session/', views.get_session, name='get-seesion'),
    path('delete-session/', views.delete_session,name='delete-session')
    
]
