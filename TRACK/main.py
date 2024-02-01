
import phonenumbers
from phonenumbers import geocoder 
import folium


# key carefull use to  be some time only  
Key = "ee8b118e18ff4196b15c7f25db1fee74"

number = input("Enter phone number with country code:") 
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

# map location ke liye :key is from open cage free trial  only one time 

from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(number_location)
results = geocoder.geocode(query)

# lattitude will now by this syntax

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")


