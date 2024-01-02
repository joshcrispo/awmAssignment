# views.py
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from rest_framework.decorators import api_view
from rest_framework import generics, status
from .models import Location
from .serializers import LocationSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@login_required(login_url='login')
def home(request):
    # Fetch existing locations
    locations = Location.objects.all()

    recent_locations = Location.objects.order_by('-log_date')[:5]
    return render(request, 'home.html', {'locations': locations, 'recent_locations': recent_locations})


@api_view(['POST'])
def api_add_location(request):

    data = request.data
    comment = data.get('comment')

    coordinates_data = data.get('coordinates', {})
    latitude = coordinates_data.get('coordinates', [])[1]
    longitude = coordinates_data.get('coordinates', [])[0]

    location = Point(longitude, latitude)

    Location.objects.create(coordinates=location, comment=comment)

    serializer = LocationSerializer(location)
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to your home page
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = UserCreationForm()

    return render(request, 'accounts/registration.html', {'form': form})