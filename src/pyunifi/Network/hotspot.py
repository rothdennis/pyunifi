from .network import Network
from requests import get

class Hotspot(Network):
    
    def get_vouchers(self, site_id: str, offset: int = 0, limit: int = 25, filters: str = None):
        """
        Retrieve a paginated list of Hotspot vouchers.
        https://developer.ui.com/network/v10.1.84/getvouchers
        """
        endpoint = f"/v1/sites/{site_id}/hotspot/vouchers"
        url = f"{self.url}{endpoint}"
        params = {"offset": offset, 
                  "limit": limit, 
                  "filter": filters}
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_voucher_details(self, site_id: str, voucher_id: str):
        """
        Retrieve details of a specific Hotspot voucher.
        https://developer.ui.com/network/v10.1.84/getvoucher
        """
        endpoint = f"/v1/sites/{site_id}/hotspot/vouchers/{voucher_id}"
        url = f"{self.url}{endpoint}"
        res = get(url, headers=self.headers, verify=self.verify)
        return res.json()
