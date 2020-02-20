import requests
import json


################ LOGIN ######################
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

aresponse = requests.post(url, auth=(user, pw), verify=False)
print(aresponse)
token = aresponse.json()['Token']

############ GET CLIENT HEALTH STATS ################

curl = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"

querystring = {"timestamp": ""}

headers = {
    'X-auth-token': token
}

response = requests.get(url=curl, headers=headers, params=querystring).json()

print(json.dumps(response, indent=2, sort_keys=True))

print(f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")


scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == 'WIRELESS':
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")