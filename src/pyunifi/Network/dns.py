from .network import Network
from requests import get

class DNS(Network):
    
    def get_dns_policies(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all DNS policies on a site.
        https://developer.ui.com/network/v10.1.84/getdnspolicypage
        """
        
        endpoint = f"/v1/sites/{site_id}/acl-rules"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_dns_policy(self, site_id: str, policy_id: str):
        """
        Retrieve specific DNS policy.
        https://developer.ui.com/network/v10.1.84/getdnspolicy
        """
        
        endpoint = f"/v1/sites/{site_id}/dns/policies/{policy_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()