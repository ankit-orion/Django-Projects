from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('polls/<int:poll_id>/', views.poll_detail_view, name='detail'),
]
