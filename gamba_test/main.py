import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint as pp

class PinnacleAPIClient:
    BASE_URL = "https://api.pinnacle.com/v1"
    
    def __init__(self, username, password):
        self.auth = HTTPBasicAuth(username, password)
    
    def get_sports(self):
        """Fetch a list of available sports."""
        url = f"{self.BASE_URL}/sports"
        response = requests.get(url, auth=self.auth)
        return self._handle_response(response)
    
    def get_odds(self, sport_id, league_id=None, odds_format='DECIMAL'):
        """Fetch odds for a specific sport (and optional league)."""
        url = f"{self.BASE_URL}/odds?sportId={sport_id}&oddsFormat={odds_format}"
        if league_id:
            url += f"&leagueId={league_id}"
        response = requests.get(url, auth=self.auth)
        return self._handle_response(response)
    
    def get_settled_bets(self):
        """Fetch settled bets to see which bets have paid out."""
        url = f"{self.BASE_URL}/bets/settled"
        response = requests.get(url, auth=self.auth)
        return self._handle_response(response)
    
    def _handle_response(self, response):
        """Handle API response and return JSON data or raise an error."""
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")


