from .network import Network
from requests import get

class Support(Network):
    
    def get_wan_interfaces(self, site_id: str, offset: int = 0, limit: int = 25):
        """
        Returns available WAN interface definitions for a given site, including identifiers and names. Useful for network and NAT configuration.
        https://developer.ui.com/network/v10.1.84/getwansoverviewpage
        """
        
        endpoint = f"/v1/sites/{site_id}/wans"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_site_to_site_vpn_tunnels(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all site-to-site VPN tunnels on a site.
        https://developer.ui.com/network/v10.1.84/getsitetositevpntunnelpage
        """
        
        endpoint = f"/v1/sites/{site_id}/vpn/site-to-site-tunnels"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_vpn_servers(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all VPN servers on a site.
        https://developer.ui.com/network/v10.1.84/getvpnserverpage
        """
        
        endpoint = f"/v1/sites/{site_id}/vpn/servers"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_radius_profiles(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Returns available RADIUS authentication profiles, including configuration origin metadata.
        https://developer.ui.com/network/v10.1.84/getradiusprofileoverviewpage
        """
        
        endpoint = f"/v1/sites/{site_id}/radius/profiles"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_device_tags(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Returns all device tags defined within a site, which can be used for WiFi Broadcast assignments.
        https://developer.ui.com/network/v10.1.84/getdevicetagpage
        """
        
        endpoint = f"/v1/sites/{site_id}/device-tags"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_dpi_application_categories(self, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Returns predefined Deep Packet Inspection (DPI) application categories used for traffic identification and filtering.
        https://developer.ui.com/network/v10.1.84/getdpiapplicationcategories
        """
        
        endpoint = "/v1/dpi/categories"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_dpi_applications(self, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Lists DPI-recognized applications grouped under categories. Useful for firewall or traffic analytics integration.
        https://developer.ui.com/network/v10.1.84/getdpiapplications
        """
        
        endpoint = "/v1/dpi/applications"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_countries(self, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Returns ISO-standard country codes and names, used for region-based configuration or regulatory compliance.
        https://developer.ui.com/network/v10.1.84/getcountries
        """
        
        endpoint = "/v1/countries"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()