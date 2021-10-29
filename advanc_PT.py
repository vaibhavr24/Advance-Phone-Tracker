import phonenumbers as ph
from phonenumbers import geocoder, carrier
import opencage as oc
from opencage.geocoder import OpenCageGeocode
import folium


# API for location
key = '71fa25e58e6a48db8d3788bf254dc587'

number = input('Enter number as follow +(country code)(number): ')

mainnum = ph.parse(number)

cntloc = geocoder.description_for_number(mainnum,'en')
serpro = carrier.name_for_number(mainnum,'en')

geocoder = OpenCageGeocode(key)

query = str(cntloc)

rslt = geocoder.geocode(query)
# print(rslt)

latitude = rslt[0]['geometry']['lat']
longitude = rslt[0]['geometry']['lng']

print(latitude,longitude)

mymap = folium.Map(location = [latitude,longitude],zm = 9)

folium.Marker([latitude,longitude], popup=cntloc).add_to((mymap))
 
mymap.save('location.html')