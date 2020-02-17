
# DevNet Marc-Andre Theriault
# Imports the required Request and urlopen libraries.
# Constructs a request to the CMX URI.
# Adds basic authentication to the request.
# Opens the request and gets a response from the CMX URI.
# Parses the response as a string and prints it to the console.

from urllib.request import Request, urlopen
import json


req = Request('https://cmxlocationsandbox.cisco.com/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
response = urlopen(req)
response_string = response.read().decode('utf-8')
#print(response_string)
json_object = json.loads(response_string)
#print(json.dumps(json_object, sort_keys=True, indent=4))

# Get only the information needed
accessPoints = json_object['accessPoints']
for ap in accessPoints:
    print("Access Point: " + ap['name'] + '\t mac: ' + ap['radioMacAddress'])


response.close()

