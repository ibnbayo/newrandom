from django.urls import path
from . views import pics_api_list_view

urlpatterns = [
    path('',pics_api_list_view, name='bio'),
    # path('pics/',pics_api_list_view, name='pic'),
]