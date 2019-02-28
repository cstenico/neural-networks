import csv
import numpy as np
import time
from geopy.geocoders import Nominatim

with open('default_features_1059_tracks.txt', mode='r') as infile:
    reader = csv.reader(infile, delimiter=',')
    songs = []
    for line in reader:
        songs.append(line)
for i in range(len(songs[0])):
    for row in songs:
        row[i] = float(row[i].strip())
locations = []
geolocator = Nominatim(user_agent="stenico.camila@gmail.com")
with open('locations.txt', 'w') as file:
    for i in range(0, 5):
        lati = str(songs[i][68])
        lon = str(songs[i][69])
        file.write(geolocator.reverse(lati + ', ' + lon, language='en').address.encode('utf-8'))
        file.write(';')
        print i
        time.sleep(1)