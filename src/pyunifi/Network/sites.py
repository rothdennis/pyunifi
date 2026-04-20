from .network import Network
from requests import get

class Sites(Network):
    
    def get_local_sites(self, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of local sites managed by this Network application. Site ID is required for other UniFi Network API calls.
        https://developer.ui.com/network/v10.1.84/getsiteoverviewpage
        """
        endpoint = "/v1/sites"
        url = f"{self.url}{endpoint}"
        params = {
            "offset": offset,
            "limit": limit,
            "filter": filter
        }
        
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        
        return res.json()