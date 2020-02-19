# DevNet CCNA ACI toolkit show all hosts connected to the fabric
# Marc-Andre Theriault martheri@cisco.com


import acitoolkit.acitoolkit as aci
from tabulate import tabulate

LOGIN = "admin"
PASSWORD = "ciscopsdt"
URL = "https://sandboxapicdc.cisco.com"

session = aci.Session(URL, LOGIN, PASSWORD)
session.login()

data = []
endpoints = aci.Endpoint.get(session)
for ep in endpoints:
    epg = ep.get_parent()
    app_profile = epg.get_parent()
    tenant = app_profile.get_parent()
    data.append((ep.mac, ep.ip, ep.if_name, ep.encap,
                 tenant.name, app_profile.name, epg.name))

# Display the data downloaded
print(tabulate(data, headers=["MACADDRESS", "IPADDRESS", "INTERFACE",
                              "ENCAP", "TENANT", "APP PROFILE", "EPG"]))



