import gmplot
import requests
import os
import csv

# Create the map plotter:
apikey = 'AIzaSyDil4ygmmAbn8L2qit_AOivek7nIa82Ozs' # (your API key here)
gmap = gmplot.GoogleMapPlotter(0, 0, 2, apikey=apikey)

# Get lat, lon of IP
##ip_addr = '73.9.149.180'
##api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip_addr)
##response = requests.get(api_url, headers={'X-Api-Key': 'gUMd15sgzurPzg2Smfr1rw==kchzmYCyqNNqGklW'})
##if response.status_code == requests.codes.ok:
##    print(response.text)
##else:
##    print("Error:", response.status_code, response.text)


mal = []
saf = []

# Run netstat
def netstat():
    netstat = os.popen("netstat -nb").readlines()
    return onlyIP(netstat)

#Collect only public IP from Netstat
def onlyIP(output):
    output = output[1:20]
    lst = [e[44:67] for e in output]
    return lst
    
    
# Mark a hidden gem:
gmap.marker(32.5232, -92.6379, color='cornflowerblue')

# Draw the map to an HTML file:
gmap.draw('map.html')

# Read csv file
with open('addresses.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines)
        if(lines[1] == 'M'):
            mal.append(lines[0])
        else:
            saf.append(lines[0])

print(mal)





#print(netstat())
