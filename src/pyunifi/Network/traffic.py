from .network import Network
from requests import get

class Traffic(Network):
    
    def get_traffic_matching_list(self, site_id: str, traffic_matching_list_id: str):
        """
        Get an existing traffic matching list on a site.
        https://developer.ui.com/network/v10.1.84/gettrafficmatchinglist
        """
        
        endpoint = f"/v1/sites/{site_id}/traffic-matching-lists/{traffic_matching_list_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()
    
    def get_traffic_matching_lists(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve all traffic matching lists on a site.
        https://developer.ui.com/network/v10.1.84/gettrafficmatchinglists
        """
        
        endpoint = f"/v1/sites/{site_id}/traffic-matching-lists"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()