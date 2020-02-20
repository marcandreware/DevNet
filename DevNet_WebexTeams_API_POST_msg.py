# DevNet CCNA Study
# Marc-Andre Theriault
# Send English words as one argument on the command line and get a French translation from the ToFrench bot.

import sys
import requests
requests.packages.urllib3.disable_warnings()

endpoint = "https://api.ciscospark.com/v1"
resource = "/messages"
access_token = "{yourToken}}"
headers = {
    "content-type": "application/json",
    "authorization": "Bearer " + access_token
}
body = {
    "toPersonEmail": "ToFrench@webex.bot",
    "text": str(sys.argv[1])
}
url = endpoint + resource

response = requests.post(url, headers=headers, json=body, verify=False)
print(response)




