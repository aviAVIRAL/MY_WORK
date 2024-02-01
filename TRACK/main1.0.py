




import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

print()
def validate_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number, "US")
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

# imp key only limited trial 
# map location ke liye

Key = "ee8b118e18ff4196b15c7f25db1fee74"

number = input("Enter phone number with country code:")

if validate_phone_number(number):
    print("Valid phone number.")

    check_number = phonenumbers.parse(number)
    number_location = geocoder.description_for_number(check_number, "en")
    print(number_location)

#    map google crome  desktop
    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider, "en"))

    geocoder_instance = OpenCageGeocode(Key)
    query = str(number_location)
    results = geocoder_instance.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)

    map_location = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=number_location).add_to(map_location)
    map_location.save("GoogleMaps.html")
else:
    print("Invalid phone number. Please enter a valid phone number.")

print()


