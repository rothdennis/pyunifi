from .network import Network
from requests import get

class Networks(Network):
    
    def get_network_details(self, site_id: str, network_id: str) -> dict:
        """
        Retrieve detailed information about a specific network.
        https://developer.ui.com/network/v10.1.84/getnetworkdetails
        """
        endpoint = f"/v1/sites/{site_id}/networks/{network_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()

    def get_networks(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all Networks on a site.
        https://developer.ui.com/network/v10.1.84/getnetworksoverviewpage
        """
        endpoint = f"/v1/sites/{site_id}/networks"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}

        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_network_references(self, site_id: str, network_id: str):
        """
        Retrieve a list of all Networks on a site with only the id and name.
        https://developer.ui.com/network/v10.1.84/getnetworkreferences
        """
        endpoint = f"/v1/sites/{site_id}/networks/{network_id}/references"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()