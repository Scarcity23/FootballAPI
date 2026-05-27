from .api import APIWrapper

class Football:
    def __init__(self, api_key: str):
        self._api = APIWrapper(api_key)

    def get_countries(self, name: str = None, code: str = None, search: str = None):
        """
        Fetch country from the API.

        Args:
            name     (str): The name of the country
            code     (str): The 3-character code of the country e.g. "ARS"
            search   (str): The name of the country (min 3 characters)
        """
        params = {k: v for k, v in {
            'name':    name,
            'code':    code,
            'search':  search,
        }.items() if v is not None}

        return self._api.get("/country", params)
    
    def get_teams(self, id: int = None, name: str = None, league: int = None, season: int = None,
                country: str = None, code: str = None, venue: int = None, search: str = None):
        """
        Fetch teams from the API.

        Args:
            id       (int): The id of the team
            name     (str): The name of the team
            league   (int): The id of the league
            season   (int): The season of the league, 4 digits e.g. 2024
            country  (str): The country name of the team
            code     (str): The 3-character code of the team e.g. "ARS"
            venue    (int): The id of the venue
            search   (str): The name or country name of the team (min 3 characters)
        """
        params = {k: v for k, v in {
            'id':      id,
            'name':    name,
            'league':  league,
            'season':  season,
            'country': country,
            'code':    code,
            'venue':   venue,
            'search':  search,
        }.items() if v is not None}

        return self._api.get("/teams", params)