class Network:
    
    def __init__(self, api_key, hostname=None, console_id=None, verify=True):
        self.verify = verify
        self.headers = {
            'Accept': 'application/json',
            'X-API-Key': api_key
            }
        
        if not hostname and not console_id:
            raise ValueError("Either hostname or console_id must be provided.")
        
        if hostname and console_id:
            raise ValueError("Only one of hostname or console_id should be provided.")
        
        if hostname:
            self.url = f"https://{hostname}/proxy/network/integration"
        else:
            self.url = f"https://api.ui.com/v1/connector/consoles/{console_id}/proxy/network/integration/"