from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_pin/', views.add_pin, name='add_pin'),
]