from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_application, name='job_application'),
    path('success/', views.success_view, name='success'),
]
