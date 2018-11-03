from access_token import token
import googlemaps as gm
token = token()

gmaps = gm.Client(key=token)
#location = gmaps.geolocate()