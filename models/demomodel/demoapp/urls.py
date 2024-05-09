from django.urls import path
from .import views 
urlpatterns = [
      path("blogpost/<int:id>", views.blogpost)
 ]
 
