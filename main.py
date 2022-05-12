import gmplot
import requests
import os
import csv
import json
import geopy.distance
from geopy.geocoders import Nominatim

# Create the map plotter:
apikey = 'AIzaSyDil4ygmmAbn8L2qit_AOivek7nIa82Ozs' # (your API key here)
gmap = gmplot.GoogleMapPlotter(0, 0, 2, apikey=apikey)
geolocator = Nominatim(user_agent="geoapiExercises")

x = []
y = []
gmap.marker(32.5232, -92.6379, color="yellow")

# Get lat, lon of IP
def geo(ip_addr):
    
    api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip_addr)
    response = requests.get(api_url, headers={'X-Api-Key': 'gUMd15sgzurPzg2Smfr1rw==kchzmYCyqNNqGklW'})

    if response.status_code == requests.codes.ok:
        data = response.text
        parse_json = json.loads(data)
        x.append(parse_json['lat'])
        y.append(parse_json['lon'])
        return parse_json['lat'], parse_json['lon']
    
    else:
        print("Error:", response.status_code, response.text)

#plot safe address
def plotSaf(x,y):
    gmap.marker(x, y, color="green")

#plot malicious address
def plotMal(x,y):
    gmap.marker(x, y, color="red")   

# Read csv file
with open('ip_list.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
  next(csvFile)
  # displaying the contents of the CSV file
  for lines in csvFile:

        print(lines)

        #determine if IP address is safe or malicious
        if(lines[1] == 'M'):
            cords = geo(lines[0])
            plotMal(cords[0], cords[1])
            
        
        else:
            
            cords = geo(lines[0])
            plotSaf(cords[0], cords[1])
            

# make a list of each coordinate from ip address and compare distance with each coordiante
z = list(zip(x,y))

#print(z)
for i in range(len(z)):
    ran = 0
    for j in range(i + 1, len(z)):
        if (geopy.distance.geodesic(z[i],z[j]).miles < 300):
            ran = ran + 1 
    if ran > 2:
        latitude = "25.594095"
        longitude = "85.137566"
        location = geolocator.reverse(latitude+","+longitude)
        address = location.raw['address']
        country = address.get('country', '')
        print(country)
        
    
# Draw the map to an HTML file:
gmap.draw('map.html')
