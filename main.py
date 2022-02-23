import gmplot
import requests
import os

# Create the map plotter:
apikey = 'AIzaSyCT00gibgn-VBeOAoDjIEnSSq5LlRMpOEs' # (your API key here)
gmap = gmplot.GoogleMapPlotter(0, 0, 2, apikey=apikey)

# Get lat, lon of IP
##ip_addr = '73.9.149.180'
##api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip_addr)
##response = requests.get(api_url, headers={'X-Api-Key': 'gUMd15sgzurPzg2Smfr1rw==kchzmYCyqNNqGklW'})
##if response.status_code == requests.codes.ok:
##    print(response.text)
##else:
##    print("Error:", response.status_code, response.text)

# Run netstat
output_command = os.popen("netstat -nb").readlines()
output_command = output_command[1:20]
lst = [e[44:67] for e in output_command]
print(lst)
# Mark a hidden gem:
gmap.marker(37.770776, -122.461689, color='cornflowerblue')

# Draw the map to an HTML file:
gmap.draw('map.html')
