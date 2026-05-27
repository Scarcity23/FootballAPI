from football import Football

fb = Football("api-key")
print(fb.get_teams(season=2026, league=253))