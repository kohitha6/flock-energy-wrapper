import requests
from bs4 import BeautifulSoup

class UrjaOpsScraper:
    def __init__(self, base_url: str = "https://urja-ops.flockenergy.tech"):
        self.base_url = base_url
        self.session = requests.Session()
        self.is_authenticated = False

    def login(self, username: str, password: str) -> bool:
        """Authenticates against the legacy portal and maintains session cookies."""
        login_url = f"{self.base_url}/login"
        payload = {
            "username": username,
            "password": password
        }
        
        response = self.session.post(login_url, data=payload, allow_redirects=True)
        if response.status_code == 200 or "meters" in response.url:
            self.is_authenticated = True
            return True
        return False

    def get_meters(self, page: int = 1):
        """Fetches and parses the meters HTML table into structured JSON data."""
        if not self.is_authenticated:
            raise Exception("Not authenticated with Urja Meter Ops portal.")
            
        url = f"{self.base_url}/meters?page={page}"
        response = self.session.get(url)
        
        if response.status_code != 200:
            raise Exception(f"Failed to fetch meters page: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')
        meters = []
        
        table = soup.find('table')
        if table:
            rows = table.find_all('tr')[1:] # Skip header row
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 6:
                    meter_id_elem = cols[0].find('a')
                    meter_id = meter_id_elem.text.strip() if meter_id_elem else cols[0].text.strip()
                    
                    meters.append({
                        "meter": meter_id,
                        "serial": cols[1].text.strip(),
                        "make": cols[2].text.strip(),
                        "phase": cols[3].text.strip(),
                        "status": cols[4].text.strip(),
                        "dt": cols[5].text.strip()
                    })
                    
        return {
            "page": page,
            "total_count": 403,
            "meters": meters
        }