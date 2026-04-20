from configparser import ConfigParser
from pyunifi import *
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = ConfigParser()
config.read("config.ini")

API_KEY = config.get("unifi", "api_key")
HOSTNAME = config.get("unifi", "hostname")
SITE_ID = config.get("unifi", "site_id")
DEVICE_ID = config.get("unifi", "device_id")
CLIENT_ID = config.get("unifi", "client_id")
NETWORK_ID = config.get("unifi", "network_id")

# app = Application(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(app.get_info(), indent=4))

# sites = Sites(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(sites.get_local_sites(), indent=4))

# devices = Devices(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(devices.get_adopted_devices(SITE_ID), indent=4))
# print(json.dumps(devices.get_adopted_device_details(SITE_ID, DEVICE_ID), indent=4))
# print(json.dumps(devices.get_latest_adopted_device_statistics(SITE_ID, DEVICE_ID), indent=4))
# print(json.dumps(devices.get_devices_pending_adoption(SITE_ID), indent=4))

# clients = Clients(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(clients.get_connected_clients(SITE_ID), indent=4))
# print(json.dumps(clients.get_connected_client_details(SITE_ID, CLIENT_ID), indent=4))

networks = Networks(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(networks.get_networks(SITE_ID), indent=4))
# print(json.dumps(networks.get_network_details(SITE_ID, NETWORK_ID), indent=4))
print(json.dumps(networks.get_network_references(SITE_ID, NETWORK_ID), indent=4))