# DevNet CCNA Study
# Marc-Andre Theriault
# Returns 5 Webex Teams rooms names and ID's with the most recent activity.

import requests
requests.packages.urllib3.disable_warnings()

endpoint = "https://api.ciscospark.com/v1"
resource = "/rooms"
access_token = "{yourtoken}"
headers = {
    "content-type": "application/json",
    "authorization": "Bearer " + access_token
}
params = {
    "sortBy": "lastactivity",
    "max": "5"
}
url = endpoint + resource

response = requests.get(url, headers=headers, params=params, verify=False)

try:
    for room in response.json()['items']:
        print("Room Name: " + room['title'])
        print("Room ID: " + room['id'])
except Exception:
    print("something went wrong!")
finally:
    print(response)


