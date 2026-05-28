from .api import APIWrapper

class Football:
    def __init__(self, api_key: str):
        self._api = APIWrapper(api_key)

    def get_countries(self, name: str = None, code: str = None, search: str = None):
        """
        Get the list of available countries for the leagues endpoint.

        Args:
            name     (str): The name of the country
            code (str): The Alpha code of the country e.g. "FR", "GB-ENG"
            search   (str): The name of the country ( = 3 characters)
        """
        params = {k: v for k, v in {
            'name':    name,
            'code':    code,
            'search':  search,
        }.items() if v is not None}

        return self._api.get("/countries", params)
    
    def get_leagues(self, id: int = None, name: str = None, country: str = None, code: str = None,
                    season: int = None, team: int = None, type: str = None, current: str = None, 
                    search: str = None, last: int = None):
        """
        Get the list of available leagues and cups.

        Args:
            id       (int): The id of the league
            name     (str): The name of the league
            country  (str): The country name of the league
            code     (str): The Alpha code of the country
            season   (int): The season of the league, 4 digits e.g. 2024
            team     (int): The id of the team
            type     (str): The type of the league, enum "league" "cup"
            current  (str): The state of the league, enum "true" "false"
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
    
    def get_team_statistics(self, league: int, season: int, team: int, date: str = None):
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
    
    def get_team_seasons(self, team: int):
        """
        Get the list of seasons available for a team.
        
        Args:
            team (int): The id of the team (required)
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

    def get_venues(self, id: int = None, name: str = None, city: str = None, country: str = None,
                   search: str = None):
        """
        Get the list of available venues.

        Args:
            id       (int): The id of the venue
            name     (str): The name of the venue
            city     (str): The city of the venue
            country  (str): The country name of the venue
            search   (str): The name, city of the country of the venue (min 3 char)
        """
        params = {k: v for k, v in {
            'id':      id,
            'name':    name,
            'city':    city,
            'country': country,
            'search':  search
        }.items() if v is not None}

        return self._api.get("/venues", params)
    
    def get_standings(self, season: int, league: int = None, team: int = None):
        """
        Get the standings for a league or a team.

        Args:
            season (int): The season of the league, 
                4 digits e.g. 2024 (required)
            league   (int): The id of the league
            team     (int): The id of the team
        """

        params = {k: v for k, v in {
            'season':  season,
            'league':  league,
            'team':    team
        }.items() if v is not None}

        return self._api.get("/standings", params)
    
    def get_fixture_rounds(self, league: int, season: int, current: str = None,
                       dates: str = None, timezone: str = None):
        """
        Get the rounds for a league or a cup.

        Args:
            league    (int): The id of the league (required)
            season    (int): The season of the league, 4 digits e.g. 2024 (required)
            current   (str): The current round only, enum "true" "false"
            dates     (str): Add the dates of each round in the response, enum "true" "false"
            timezone  (str): A valid timezone from the endpoint Timezone
        """
        params = {k: v for k, v in {
            'league':   league,
            'season':   season,
            'current':  current,
            'dates':    dates,
            'timezone': timezone,
        }.items() if v is not None}

        return self._api.get("/fixtures/rounds", params)
    
    def get_fixtures(self, id: int = None, ids: str = None, live: str = None,
                 date: str = None, league: int = None, season: int = None,
                 team: int = None, last: int = None, next: int = None,
                 from_date: str = None, to_date: str = None, round: str = None,
                 status: str = None, venue: int = None, timezone: str = None):
        """
        Get fixtures.

        Args:
            id        (int): The id of the fixture
            ids       (str): One or more fixture ids, format "id-id-id" (max 20)
            live      (str): All or several league ids, enum "all" "id-id"
            date      (str): A valid date, format YYYY-MM-DD
            league    (int): The id of the league
            season    (int): The season of the league, 4 digits e.g. 2024
            team      (int): The id of the team
            last      (int): For the X last fixtures (max 2 digits)
            next      (int): For the X next fixtures (max 2 digits)
            from_date (str): A valid date, format YYYY-MM-DD
            to_date   (str): A valid date, format YYYY-MM-DD
            round     (str): The round of the fixture
            status    (str): One or more fixture status short, enum "NS" "NS-PST-FT"
            venue     (int): The venue id of the fixture
            timezone  (str): A valid timezone from the endpoint Timezone
        """
        params = {k: v for k, v in {
            'id':       id,
            'ids':      ids,
            'live':     live,
            'date':     date,
            'league':   league,
            'season':   season,
            'team':     team,
            'last':     last,
            'next':     next,
            'from':     from_date,
            'to':       to_date,
            'round':    round,
            'status':   status,
            'venue':    venue,
            'timezone': timezone,
        }.items() if v is not None}

        return self._api.get("/fixtures", params)
    
    def get_headtohead(self, h2h: str, date: str = None, league: int = None,
                   season: int = None, last: int = None, next: int = None,
                   from_date: str = None, to_date: str = None, status: str = None,
                   venue: int = None, timezone: str = None):
        """
        Get head to head between two teams.

        Args:
            h2h       (str): The ids of the two teams, format "ID-ID" (required)
            date      (str): A valid date, format YYYY-MM-DD
            league    (int): The id of the league
            season    (int): The season of the league, 4 digits e.g. 2024
            last      (int): For the X last fixtures
            next      (int): For the X next fixtures
            from_date (str): A valid date, format YYYY-MM-DD
            to_date   (str): A valid date, format YYYY-MM-DD
            status    (str): One or more fixture status short, enum "NS" "NS-PST-FT"
            venue     (int): The venue id of the fixture
            timezone  (str): A valid timezone from the endpoint Timezone
        """
        params = {k: v for k, v in {
            'h2h':      h2h,
            'date':     date,
            'league':   league,
            'season':   season,
            'last':     last,
            'next':     next,
            'from':     from_date,
            'to':       to_date,
            'status':   status,
            'venue':    venue,
            'timezone': timezone,
        }.items() if v is not None}

        return self._api.get("/fixtures/headtohead", params)

    def get_fixture_statistics(self, fixture: int, team: int = None,
                           type: str = None, half: str = None):
        """
        Get the statistics for one fixture.

        Args:
            fixture (int): The id of the fixture (required)
            team    (int): The id of the team
            type    (str): The type of statistics
            half    (str): Add the halftime statistics in the response, enum "true" "false"
                        Data available from 2024 season onwards
        """
        params = {k: v for k, v in {
            'fixture': fixture,
            'team':    team,
            'type':    type,
            'half':    half,
        }.items() if v is not None}

        return self._api.get("/fixtures/statistics", params)

    # Available event types:
    # Goal  - "Normal Goal", "Own Goal", "Penalty", "Missed Penalty"
    # Card  - "Yellow Card", "Red Card"
    # Subst - "Substitution [1, 2, 3...]"
    # Var   - "Goal cancelled", "Penalty confirmed"
    def get_fixture_events(self, fixture: int, team: int = None,
                        player: int = None, type: str = None):
        """
        Get the events from a fixture.

        Args:
            fixture (int): The id of the fixture (required)
            team    (int): The id of the team
            player  (int): The id of the player
            type    (str): The type of event
                        Goal  - "Normal Goal", "Own Goal", "Penalty", "Missed Penalty"
                        Card  - "Yellow Card", "Red Card"
                        Subst - "Substitution [1, 2, 3...]"
                        Var   - "Goal cancelled", "Penalty confirmed"
        """
        params = {k: v for k, v in {
            'fixture': fixture,
            'team':    team,
            'player':  player,
            'type':    type,
        }.items() if v is not None}

        return self._api.get("/fixtures/events", params)

    def get_fixture_lineups(self, fixture: int, team: int = None,
                        player: int = None, type: str = None):
        """
        Get the lineups for a fixture.

        Args:
            fixture (int): The id of the fixture (required)
            team    (int): The id of the team
            player  (int): The id of the player
            type    (str): The type
        """
        params = {k: v for k, v in {
            'fixture': fixture,
            'team':    team,
            'player':  player,
            'type':    type,
        }.items() if v is not None}

        return self._api.get("/fixtures/lineups", params)

    def get_fixture_players(self, fixture: int, team: int = None):
        """
        Get the player statistics from one fixture.

        Args:
            fixture (int): The id of the fixture (required)
            team    (int): The id of the team
        """
        params = {k: v for k, v in {
            'fixture': fixture,
            'team':    team,
        }.items() if v is not None}

        return self._api.get("/fixtures/players", params)

    def get_injuries(self, league: int = None, season: int = None, fixture: int = None,
                 team: int = None, player: int = None, date: str = None,
                 ids: str = None, timezone: str = None):
        """
        Get the list of players not participating in fixtures e.g. suspended, injured.
        Data available from April 2021 onwards.

        Args:
            league   (int): The id of the league
            season   (int): The season of the league, 4 digits e.g. 2024
                            Required when using league, team or player parameters
            fixture  (int): The id of the fixture
            team     (int): The id of the team
            player   (int): The id of the player
            date     (str): A valid date, format YYYY-MM-DD
            ids      (str): One or more fixture ids, format "id-id-id" (max 20)
            timezone (str): A valid timezone from the endpoint Timezone
        """
        params = {k: v for k, v in {
            'league':   league,
            'season':   season,
            'fixture':  fixture,
            'team':     team,
            'player':   player,
            'date':     date,
            'ids':      ids,
            'timezone': timezone,
        }.items() if v is not None}

        return self._api.get("/injuries", params)

    def get_player_seasons(self, player: int = None):
        """
        Get all available seasons for player statistics.

        Args:
            player (int): The id of the player
        """
        params = {k: v for k, v in {
            'player': player,
        }.items() if v is not None}

        return self._api.get("/players/seasons", params)

    def get_player_profiles(self, player: int = None, search: str = None, page: int = None):
        """
        Get the list of all available players.

        Args:
            player (int): The id of the player
            search (str): The lastname of the player (min 3 characters)
            page   (int): Page number for pagination, default 1
        """
        params = {k: v for k, v in {
            'player': player,
            'search': search,
            'page':   page,
        }.items() if v is not None}

        return self._api.get("/players/profiles", params)

    def get_players(self, id: int = None, team: int = None, league: int = None,
                    season: int = None, search: str = None, page: int = None):
        """
        Get players statistics.

        Args:
            id     (int): The id of the player
            team   (int): The id of the team
            league (int): The id of the league
            season (int): The season of the league, 4 digits e.g. 2024
                        Required with id, league or team parameters
            search (str): The name of the player (min 4 characters)
                        Requires league or team parameters
            page   (int): Page number for pagination, default 1 (20 per page)
        """
        params = {k: v for k, v in {
            'id':     id,
            'team':   team,
            'league': league,
            'season': season,
            'search': search,
            'page':   page,
        }.items() if v is not None}

        return self._api.get("/players", params)
    
    def get_squads(self, team: int = None, player: int = None):
        """
        Get the current squad of a team, or the set of teams associated with a player.

        Args:
            team   (int): The id of the team, returns the current squad
            player (int): The id of the player, returns all associated teams
        """
        params = {k: v for k, v in {
            'team':   team,
            'player': player,
        }.items() if v is not None}

        return self._api.get("/players/squads", params)

    def get_player_teams(self, player: int):
        """
        Get the list of teams and seasons a player has played in during their career.

        Args:
            player (int): The id of the player (required)
        """
        params = {k: v for k, v in {
            'player': player,
        }.items() if v is not None}

        return self._api.get("/players/teams", params)





