# DevNet CCNA Study
# Marc-Andre Theriault


import json
import requests
requests.packages.urllib3.disable_warnings()

endpoint = "https://api.ciscospark.com/v1"
resource = "/people"
access_token = "{yourtoken}"
headers = {
    "content-type": "application/json",
    "authorization": "Bearer " + access_token
}
params = "?email={youremail}"
url = endpoint + resource + params
response = requests.get(url, headers=headers, verify=False)

print(response)
print(response.json())

person = response.json()['items'][0]
print("Name " + person['displayName'])
print("Email " + person['emails'][0])


