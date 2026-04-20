from .network import Network
from requests import get

class Application(Network):
        
    def get_info(self):
        """
        Retrieve general information about the UniFi Network application.
        https://developer.ui.com/network/v10.1.84/getinfo
        """
        
        endpoint = "/v1/info"
        url = f"{self.url}{endpoint}"
        
        res = get(url, headers=self.headers, verify=self.verify)
        
        return res.json()