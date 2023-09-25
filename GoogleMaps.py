import googlemaps
import pprint

API = "AIzaSyAk7vMYu6vq0Jfyq3F-Yk1864mBfZnYTcs"

client = googlemaps.Client(key = API)
print(client)

start = input("Start: ")
# end = input("End: ")
#distance = client.directions(start,end)
geocode_result = client.geocode(start)
latitude = geocode_result[0]['geometry']['location']['lat']
longtitude = geocode_result[0]['geometry']['location']['lng']
print(latitude)
print(longtitude)