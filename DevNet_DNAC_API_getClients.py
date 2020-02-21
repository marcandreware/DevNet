
//'x-auth-token': 'x-auth-token-value'
 //'content-type': 'application/json'
 import http.client

conn = http.client.HTTPSConnection("10.85.57.25")

conn.request("GET", "/dna/intent/api/v1/client-health?timestamp=<timestamp>")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))