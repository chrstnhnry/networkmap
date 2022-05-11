import gmplot
import requests
import os
import csv
import json

# Create the map plotter:
apikey = 'AIzaSyDil4ygmmAbn8L2qit_AOivek7nIa82Ozs' # (your API key here)
gmap = gmplot.GoogleMapPlotter(0, 0, 2, apikey=apikey)

# Get lat, lon of IP
def geo(ip_addr):
    #ip_addr = '73.9.149.180'
    api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip_addr)
    response = requests.get(api_url, headers={'X-Api-Key': 'gUMd15sgzurPzg2Smfr1rw==kchzmYCyqNNqGklW'})

    if response.status_code == requests.codes.ok:
        data = response.text
        parse_json = json.loads(data)
        return parse_json['lat'], parse_json['lon']
    #print(parse_json)
    #print(active_case) 
    else:
        print("Error:", response.status_code, response.text)

#plot safe address
def plotSaf(x,y):
    gmap.marker(x,y,color="green")

#plot malicious address
def plotMal(x,y):
    gmap.marker(x,y,color="red")   

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
            #print(lines[0])
            cords = geo(lines[0])
            #print(geo('111.111.111.111'))
            plotMal(cords[0], cords[1])
            break
        else:
            print(lines[0])
            #cords = geo(lines[0])
            #plotSaf(cords[0], cords[1])
            break


    
# Draw the map to an HTML file:
gmap.draw('map.html')
