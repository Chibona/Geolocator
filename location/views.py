

import json
import requests
from django.http import JsonResponse
from django.shortcuts import render
from .models import Location

def index(request):
    return render(request, 'index.html')

def update_location(request):
    try:
        # Fetch the user's public IP address
        ip_response = requests.get('https://api.ipify.org?format=json')
        ip_data = ip_response.json()
        
        # Fetch location data based on the IP address
        res = requests.get(f'http://ip-api.com/json/{ip_data["ip"]}')
        location_data = res.json()

        # Save the location data to the database
        location = Location(
            ip_address=location_data.get('query'),
            city=location_data.get('city'),
            region=location_data.get('regionName'),
            country=location_data.get('country'),
            isp=location_data.get('isp'),
            lan=location_data.get('lat'),
            lon=location_data.get('lon'),
        )
        location.save()

        return JsonResponse(location_data)  # Return the location data as JSON

    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
