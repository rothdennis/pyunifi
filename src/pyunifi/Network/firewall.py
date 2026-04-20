from .network import Network
from requests import get

class Firewall(Network):
    
    def get_firewall_policy(self, site_id: str, firewall_policy_id: str):
        """
        Retrieve specific firewall policy.
        https://developer.ui.com/network/v10.1.84/getfirewallpolicy
        """
        
        endpoint = f"/v1/sites/{site_id}/firewall/policies/{firewall_policy_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()
    
    def get_firewall_policies(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a list of all firewall policies on a site.
        https://developer.ui.com/network/v10.1.84/getfirewallpolicies
        """
        
        endpoint = f"/v1/sites/{site_id}/firewall/policies?offset={offset}&limit={limit}"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_firewall_zone(self, site_id: str, firewall_zone_id: str):
        """
        Get a firewall zone on a site.
        https://developer.ui.com/network/v10.1.84/getfirewallzone
        """
        
        endpoint = f"/v1/sites/{site_id}/firewall/zones/{firewall_zone_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()
        
    
    def get_firewall_zones(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a list of all firewall zones on a site.
        https://developer.ui.com/network/v10.1.84/getfirewallzones
        """
        
        endpoint = f"/v1/sites/{site_id}/firewall/zones"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_user_defined_firewall_policy_ordering(self, site_id: str, source_firewall_zone_id: str, destination_firewall_zone_id: str):
        """
        Retrieve user-defined firewall policy ordering for a specific source/destination zone pair.
        https://developer.ui.com/network/v10.1.84/getfirewallpolicyordering
        """
        endpoint = f"/v1/sites/{site_id}/firewall/policies/ordering"
        url = f"{self.url}{endpoint}"
        params = {"sourceFirewallZoneId": source_firewall_zone_id,
                  "destinationFirewallZoneId": destination_firewall_zone_id}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()