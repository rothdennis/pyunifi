from .network import Network
from requests import get

class ACL(Network):
    
    def get_acl_rules(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all ACL rules on a site.
        https://developer.ui.com/network/v10.1.84/getaclrulepage
        """
        
        endpoint = f"/v1/sites/{site_id}/acl-rules"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset,
                  "limit": limit,
                  "filter": filter}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_user_defined_acl_rule_ordering(self, site_id: str):
        """
        Retrieve user-defined ACL rule ordering on a site.
        https://developer.ui.com/network/v10.1.84/getaclruleordering
        """
        
        endpoint = f"/v1/sites/{site_id}/acl-rules/ordering"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()
    
    def get_acl_rule(self, site_id: str, acl_rule_id: str):
        """
        Retrieve details of a specific ACL rule on a site.
        https://developer.ui.com/network/v10.1.84/getaclrule
        """
        
        endpoint = f"/v1/sites/{site_id}/acl-rules/{acl_rule_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()