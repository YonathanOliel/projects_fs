from django.shortcuts import render
from .models import Miluimnick
from django.http import HttpResponse, JsonResponse
from geopy.geocoders import Nominatim
import json


def main(request):
    return HttpResponse("jhonny")


def get_addresses_and_id(request):
    data = Miluimnick.objects.values('id', 'business_city', 'business_street', 'business_address')
    locations = {"coords": [] }

    for d in data:
        address = d["business_city"] + " " + d["business_street"] + " " + str(d["business_address"])
        res = address_to_coordinates_osm(d["id"], address)
        if res:
            locations["coords"].append({"id": res[0], "x": res[1], "y": res[2]})
    

    return JsonResponse(locations)


def add_business(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            if isinstance(data, dict):
                mapped_data = {
                    'first_name': data.get('first_name', ''),
                    'last_name': data.get('last_name', ''),
                    'name_business': data.get('name_business', ''),
                    'business_city': data.get('business_city', ''),
                    'business_street': data.get('business_street', ''),
                    'business_address': data.get('business_address', ''),
                    'business_type': data.get('business_type', ''),
                    'link_google_maps': data.get('link_google_maps', ''),
                }

                mapped_data = {key: value for key, value in mapped_data.items() if value}
                miluimnick = Miluimnick.objects.create(**mapped_data)

                return JsonResponse({'result': 'Data saved successfully', 'data': {'id': miluimnick.id, 'first_name': miluimnick.first_name}})
            else:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_name_and_family_name(request, id):
    data = Miluimnick.objects.filter(id=id).values('name_business', 'first_name', 'last_name')
    return HttpResponse(data)


def address_to_coordinates_osm(id, address):
    geolocator = Nominatim(user_agent="miluimap", timeout=None)
    
    try:
        location = geolocator.geocode(address)
        if location:
            latitude, longitude = location.latitude, location.longitude
            return id, latitude, longitude
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None















