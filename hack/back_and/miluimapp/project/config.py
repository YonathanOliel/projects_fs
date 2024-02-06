from geopy.geocoders import Nominatim
from project.models import Miluimnick
from django.http import HttpResponse



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






id = 9
address = "גן יבנה הר ציון 33"
coordinates = address_to_coordinates_osm(id, address)

if coordinates:
    print(f"Coordinates for '{address}': {coordinates}")
else:
    print(f"Unable to get coordinates for '{address}'")