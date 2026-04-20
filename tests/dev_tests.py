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
BROADCAST_ID = config.get("unifi", "broadcast_id")
VOUCHER_ID = config.get("unifi", "voucher_id")

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

# networks = Networks(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(networks.get_networks(SITE_ID), indent=4))
# print(json.dumps(networks.get_network_details(SITE_ID, NETWORK_ID), indent=4))
# print(json.dumps(networks.get_network_references(SITE_ID, NETWORK_ID), indent=4))

# wifi = WiFi(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(wifi.get_wifi_broadcasts(SITE_ID), indent=4))
# print(json.dumps(wifi.get_wifi_broadcast_details(SITE_ID, BROADCAST_ID), indent=4))

# hotspot = Hotspot(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(hotspot.get_vouchers(SITE_ID), indent=4))
# print(json.dumps(hotspot.get_voucher_details(SITE_ID, VOUCHER_ID), indent=4))

# firewall = Firewall(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(firewall.get_firewall_policies(SITE_ID), indent=4))
# print(json.dumps(firewall.get_firewall_zones(SITE_ID), indent=4))

# acl = ACL(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(acl.get_acl_rules(SITE_ID), indent=4))
# print(json.dumps(acl.get_user_defined_acl_rule_ordering(SITE_ID), indent=4))

# dns = DNS(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(dns.get_dns_policies(SITE_ID), indent=4))

# traffic = Traffic(API_KEY, hostname=HOSTNAME, verify=False)
# print(json.dumps(traffic.get_traffic_matching_lists(SITE_ID), indent=4))

support = Support(API_KEY, hostname=HOSTNAME, verify=False)
print(json.dumps(support.get_wan_interfaces(SITE_ID), indent=4))
print(json.dumps(support.get_site_to_site_vpn_tunnels(SITE_ID), indent=4))
print(json.dumps(support.get_vpn_servers(SITE_ID), indent=4))
print(json.dumps(support.get_radius_profiles(SITE_ID), indent=4))
print(json.dumps(support.get_device_tags(SITE_ID), indent=4))
print(json.dumps(support.get_dpi_application_categories(), indent=4))
print(json.dumps(support.get_dpi_applications(), indent=4))
print(json.dumps(support.get_countries(), indent=4))