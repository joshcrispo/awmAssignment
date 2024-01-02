# urls.py

from django.urls import path, include
from .views import home, LocationListCreateView, api_add_location, login_view, register_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home, name='home'),

    path('api/locations/', LocationListCreateView.as_view(), name='api_location_list'),
    path('api/add_location/', api_add_location, name='api_add_location'),

    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),  # Add logout URL
]

