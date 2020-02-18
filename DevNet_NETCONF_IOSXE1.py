# DevNet CCNA
# Marc-Andre Theriault martheri@cisco.com

from ncclient import manager

def netconf():
    # {'host': 'ios-xe-mgmt.cisco.com', 'username': 'developer', 'password': 'C1sco12345', 'netconf_port': 10000, 'restconf_port': 9443, 'ssh_port': 8181}
    m = manager.connect(
         host='ios-xe-mgmt.cisco.com',
         port='10000',
         username='developer',
         password='C1sco12345',
         hostkey_verify=False
         )

    for capabilities in m.server_capabilities:
        print(capabilities)

    m.close_session()


netconf()

