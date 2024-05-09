from django.urls import path, re_path
from .views import get_user_by_id, get_user_by_name

urlpatterns = [
    # Match numeric user IDs
    re_path(r'^user/(?P<user_id>\d+)/$', get_user_by_id, name='get_user_by_id'),

    # Match string user names
    re_path(r'^user/(?P<user_name>\w+)/$', get_user_by_name, name='get_user_by_name'),
]
