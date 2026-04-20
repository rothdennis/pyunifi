from .network import Network
from requests import get

class Clients(Network):
    
    def get_connected_clients(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all connected clients on a site, including physical devices (computers, smartphones) and active VPN connections.
        https://developer.ui.com/network/v10.1.84/getconnectedclientoverviewpage
        """
        endpoint = f"/v1/sites/{site_id}/clients"
        url = f"{self.url}{endpoint}"
        params = {
            "offset": offset,
            "limit": limit,
            "filter": filter
        } 
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_connected_client_details(self, site_id: str, client_id: str):
        """Retrieve detailed information about a specific connected client, including name, IP address, MAC address, connection type and access information.
        https://developer.ui.com/network/v10.1.84/getconnectedclientdetails
        """
        endpoint = f"/v1/sites/{site_id}/clients/{client_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()
