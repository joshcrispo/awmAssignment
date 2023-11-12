# views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Location
from django.contrib.gis.geos import Point


def home(request):
    # Fetch existing locations
    locations = Location.objects.all()
    return render(request, 'home.html', {'locations': locations})


@csrf_exempt
def add_pin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        comment = data.get('comment')

        # Create a Point geometry
        location = Point(float(longitude), float(latitude))

        # Save the location to the database
        Location.objects.create(coordinates=location, comment=comment)

        return JsonResponse({'success': True, 'message': 'Location added successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
