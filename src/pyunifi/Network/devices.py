from .network import Network
from requests import get

class Devices(Network):
    
    def get_adopted_devices(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of all adopted devices on a site, including basic device information.
        https://developer.ui.com/network/v10.1.84/getadopteddeviceoverviewpage
        """
        endpoint = f"/v1/sites/{site_id}/devices"
        url = f"{self.url}{endpoint}"
        params = {
            "offset": offset,
            "limit": limit,
            "filter": filter
        } 
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        return res.json()
    
    def get_adopted_device_details(self, site_id: str, device_id: str):
        """
        Retrieve detailed information about a specific adopted device, including firmware versioning, uplink state, details about device features and interfaces (ports, radios) and other key attributes.
        https://developer.ui.com/network/v10.1.84/getadopteddevicedetails
        """
        endpoint = f"/v1/sites/{site_id}/devices/{device_id}"
        url = f"{self.url}{endpoint}"
        
        res = get(url, headers=self.headers, verify=self.verify)
        
        return res.json()
    
    def get_latest_adopted_device_statistics(self, site_id: str, device_id: str):
        """
        Retrieve the latest real-time statistics of a specific adopted device, such as uptime, data transmission rates, CPU and memory utilization.
        https://developer.ui.com/network/v10.1.84/getadopteddevicelateststatistics
        """
        endpoint = f"/v1/sites/{site_id}/devices/{device_id}/statistics/latest"
        url = f"{self.url}{endpoint}"
        
        res = get(url, headers=self.headers, verify=self.verify)
        
        return res.json()
    
    def get_devices_pending_adoption(self, site_id: str, offset: int = 0, limit: int = 25, filter: str = None):
        """
        Retrieve a paginated list of devices pending adoption, including basic device information.
        https://developer.ui.com/network/v10.1.84/getpendingdevicepage
        """
        endpoint = "/v1/pending-devices"
        url = f"{self.url}{endpoint}"
        params = {
            "offset": offset,
            "limit": limit,
            "filter": filter
        }
        res = get(url, headers=self.headers, params=params, verify=self.verify)
        
        return res.json()