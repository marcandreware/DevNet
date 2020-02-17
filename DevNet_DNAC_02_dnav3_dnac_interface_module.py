# DevNet DNAC Get modules from IP
# Marc-Andre Theriault martheri@cisco.com
import requests
import sys

# Firstly obtain an authorization token to interaction with the DNAC API
DNAC_USER = "devnetuser"
DNAC_PASSWORD = "Cisco123!"
DNAC = "sandboxdnac.cisco.com"
DNAC_PORT = "443"
passed_IP = sys.argv


def get_auth_token(controller_ip=DNAC, username=DNAC_USER, password=DNAC_PASSWORD):
    """ Authenticates with controller and returns a token to be used in subsequent API invocations
    """

    login_url = "https://{0}:{1}/dna/system/api/v1/auth/token".format(controller_ip, DNAC_PORT)
    result = requests.post(url=login_url, auth=(DNAC_USER, DNAC_PASSWORD), verify=False)
    result.raise_for_status()

    token = result.json()["Token"]
    return {
        "controller_ip": controller_ip, "token": token
    }


def create_url(path, controller_ip=DNAC):
    """ Helper function to create a DNAC API endpoint URL
    """

    return "https://%s:%s/api/v1/%s" % (controller_ip, DNAC_PORT, path)


def get_url(url):

    url = create_url(path=url)
    print(url)
    token = get_auth_token()
    headers = {'X-auth-token': token['token']}
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)

    return response.json()


def ip_to_id(ip):
    return get_url("network-device/ip-address/%s" % ip)['response']['id']


def get_modules(id):
    return get_url("network-device/module?deviceId=%s" % id)


def print_info(modules):
    print("{0:30}{1:15}{2:25}{3:5}".format("Module Name","Serial Number","Part Number","Is Field Replaceable?"))
    for module in modules['response']:
        print("{moduleName:30}{serialNumber:15}{partNumber:25}{moduleType:5}".format(moduleName=module['name'],
                                                           serialNumber=module['serialNumber'],
                                                           partNumber=module['partNumber'],
                                                           moduleType=module['isFieldReplaceable']))

# Run the script and first check if an IP Address was passed on the command line
if len(sys.argv) > 1:
    print_info(get_modules(ip_to_id(passed_IP[1])))
else:
    print("Please specify IP address of device")

