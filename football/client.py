from .api import APIWrapper

class Football:
    def __init__(self, api_key: str):
        self._api = APIWrapper(api_key)

    def get_countries(self, name: str = None, code: str = None, search: str = None):
        """
        Get the list of available countries for the leagues endpoint.

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
    
    def get_leagues(self, id: int = None, name: str = None, country: str = None, code : str = None,
                    season : int = None, team: int = None, type : str = None, current : str = None, 
                    search : str = None, last : int = None):
        """
        Get the list of available leagues and cups.

        Args:
            id       (int): The id of the league
            name     (str): The name of the league
            country  (str): The country name of the league
            code     (str): The Alpha code of the country
            season   (int): The season of the league, 4 digits e.g. 2024
            team     (int): The id of the team
            type     (str): The type of the league, enum "league", "cup"
            current  (str): The state of the league, enum "true", "false"
            search   (str): The name or the country of the league (min 3 characters)
            last     (int): The X last leagues/cups added in the API (<= 2 char)
        """
        params = {k: v for k, v in {
            'id':      id,
            'name':    name,
            'country': country,  
            'code':    code,
            'season':  season,
            'team':    team,
            'type':    type,
            'current': current,
            'search':  search,
            'last':    last
        }.items() if v is not None}

        return self._api.get("/leagues", params)
    
    def get_league_seasons(self):
        """
        Get the list of available seasons.
        """

        return self._api.get("/leagues/seasons")

    def get_teams(self, id: int = None, name: str = None, league: int = None, season: int = None,
                country: str = None, code: str = None, venue: int = None, search: str = None):
        """
        Get the list of available teams.

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
    
    def get_team_statistics(self, league : int, season : int, team : int, date : str = None):
        """
        Returns the statistics of a team in relation to a given competition and season.

        Args:
            league   (int): The id of the league
            season   (int): The season of the league, 4 digits e.g. 2024
            team     (int): The id of the team
            date     (str): YYYY-MM-DD, the limit date
        """
        params = {k: v for k, v in {
            'league':  league,
            'season':  season,
            'team':    team,
            'date':    date,
        }.items() if v is not None}

        return self._api.get("/teams/statistics", params)
    
    def get_team_seasons(self, team : int):
        """
        Get the list of seasons available for a team.
        
        Args:
            team     (int): The id of the team
        """
        params = {k: v for k, v in {
            'team':    team,
        }.items() if v is not None}
        
        return self._api.get("/teams/seasons", params)  

    def get_team_countries(self):
        """
        Get the list of countries available for the teams endpoint.
        """

        return self._api.get("/teams/countries")
    
    
