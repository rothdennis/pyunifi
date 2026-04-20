from .network import Network
from requests import get

class WiFi(Network):
    
    def get_wifi_broadcasts(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all Wifi Broadcasts on a site.
        https://developer.ui.com/network/v10.1.84/getwifibroadcastpage
        """
        endpoint = f"/v1/sites/{site_id}/wifi/broadcasts"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}

        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_wifi_broadcast_details(self, site_id: str, broadcast_id: str):
        """
        Retrieve detailed information about a specific Wifi.
        https://developer.ui.com/network/v10.1.84/getwifibroadcastdetails
        """
        endpoint = f"/v1/sites/{site_id}/wifi/broadcasts/{broadcast_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()