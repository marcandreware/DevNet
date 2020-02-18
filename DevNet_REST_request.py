# DevNet CCNA Study
# Marc-Andre Theriault martheri@cisco.com

# Modules Required are: requests
import requests

# Create a GET request object "r" with URI and headers
gurl = "https://api.ciscospark.com/v1/people/me"
headers = {"authorization": "Bearer ZDVkZWIzNDgtMTMwNy00NGY0LTkxMzUtMmRjZDVkYzI0YzcyYWJiNDZjYzEtZjFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f", "content-type": "application/json"}
rg = requests.get(gurl, headers=headers)

# If the request is successful, print the body.
print("gURL " + gurl)
if rg.status_code == 200:
    print(rg.json())
    # Print the response headers
    print(rg.headers)
else:
    print("Error " + str(rg.status_code))


# Create a POST request object "rp" with URI, headers and body payload data
purl = "https://api.ciscospark.com/v1/messages"
pheaders = {"authorization": "Bearer ZDVkZWIzNDgtMTMwNy00NGY0LTkxMzUtMmRjZDVkYzI0YzcyYWJiNDZjYzEtZjFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f", "content-type": "application/json"}
payload = {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYzhkYTgwZTAtNTEwOS0xMWVhLTk1NjQtMTcwZGMyNGU5ZmRh", "text": "brauh"}

rp = requests.post(purl, headers=pheaders, json=payload)

# If the request is successful, print the body.
print("pURL " + purl)
if rp.status_code == 200:
    print(rp.json())
    # Print the response headers
    print(rp.headers)
else:
    print("Error " + str(rp.status_code))

