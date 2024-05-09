# url_app/urls.py
from django.urls import path, re_path
from .views import home, about, contact, user_profile, product_detail, category_items

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    # Regular expression for user profiles with a username
    re_path(r'^profile/(?P<username>\w+)/$', user_profile, name='user_profile'),

    # Regular expression for product details with a product ID
    re_path(r'^product/(?P<product_id>\d+)/$', product_detail, name='product_detail'),

    # Regular expression for category items with a category name
    re_path(r'^category/(?P<category>\w+)/$', category_items, name='category_items'),
]
