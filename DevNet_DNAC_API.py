# DevNet DNAC intro lab
# Marc-Andre Theriault martheri@cisco.com

import requests

# Firstly obtain an authorization token to interaction with the DNAC API
DNAC_USER = "devnetuser"
DNAC_PASSWORD = "Cisco123!"
DNAC = "https://sandboxdnac.cisco.com"
DNAC_PORT = "443"


def get_auth_token(controller_ip=DNAC, controller_port=DNAC_PORT, username=DNAC_USER, password=DNAC_PASSWORD):
    login_url = "{0}:{1}/dna/system/api/v1/auth/token".format(controller_ip, DNAC_PORT)
    result = requests.post(url=login_url, auth=(DNAC_USER, DNAC_PASSWORD), verify=False)
    result.raise_for_status()
    token = result.json()["Token"]
    return {
        "controller_ip": controller_ip,
        "token": token
    }


print(get_auth_token(DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD))

