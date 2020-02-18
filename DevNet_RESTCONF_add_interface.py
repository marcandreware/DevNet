import requests

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

payload = "{\n    \"ietf-interfaces:interface\": {\n        \"name\": \"Loopback12\",\n        \"description\": \"Configured by RESTCONF\",\n        \"type\": \"iana-if-type:softwareLoopback\",\n        \"enabled\": true,\n        \"ietf-ip:ipv4\": {\n            \"address\": [\n                {\n                    \"ip\": \"12.12.12.12\",\n                    \"netmask\": \"255.255.255.0\"\n                }\n            ]\n        }\n    }\n}"
headers = {
  'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))