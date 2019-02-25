import googlemaps
import re
import json
api_key = 'AIzaSyDrxcAGiLITBkaKC-MIf33_Eu3aCDWOByE'

gmaps = googlemaps.Client(key=api_key)

#  distance to school
def distance_to_school(loc):
    if loc == 'N/A':
        return None
    loc = loc.replace(', ', ',')
    loc = loc.replace(' ','+').rstrip()
    loc += ',Pittsburgh,PA'
    des = 'carnegie+mellon+university,PA'
    my_dist = gmaps.distance_matrix(loc, des, mode='walking')['rows'][0]['elements'][0]
    distance = my_dist['distance']['value']
    duration = my_dist['duration']['text']
    return distance,duration


#  distance between 2 points
def distance_between(loc1, loc2):
    if loc1 == 'N/A' or loc2 == 'N/A':
        return None
    loc1 = loc1.replace(', ', ',')
    loc2 = loc2.replace(', ', ',')
    loc1 = loc1.replace(' ', '+')
    loc2 = loc2.replace(' ', '+')
    my_dist = gmaps.distance_matrix(loc1, loc2, mode='walking')['rows'][0]['elements'][0]
    distance = json.load(my_dist)['distance']['value']
    duration = json.load(my_dist)['duration']['text']

    return distance,duration

#tastcase
# print(distance_between('2021 wightman street', 'carnegie mellon university'))
# {'distance': {'text': '1.8 km', 'value': 1847}, 'duration': {'text': '22 mins', 'value': 1298}, 'status': 'OK'}
# distance = distance_to_school('644 college')
# print(distance)