# DevNet CCNA ACI toolkit show all hardware connected to the fabric
# Marc-Andre Theriault martheri@cisco.com


import acitoolkit.acitoolkit as aci
from acitoolkit.aciphysobject import Pod

LOGIN = "admin"
PASSWORD = "ciscopsdt"
URL = "https://sandboxapicdc.cisco.com"

def print_inventory(item):
    """
    Display routine

    :param item: Object to print
    :return: None
    """
    for child in item.get_children():
        print_inventory(child)
    print(item.info())


def main():
    """
    Main execution routine

    :return: None
    """
    description = ('Simple application that logs on to the APIC and displays'
                   ' the physical inventory.')


    # Login to APIC
    session = aci.Session(URL, LOGIN, PASSWORD)
    session.login()

    # Print the inventory of each Pod
    pods = Pod.get(session)
    for pod in pods:
        pod.populate_children(deep=True)
        pod_name = 'Pod: %s' % pod.name
        print(pod_name)
        print('=' * len(pod_name))
        print_inventory(pod)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass