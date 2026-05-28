# Football API Wrapper

Python wrapper for the [API-Sports Football API](https://www.api-football.com/).

## Installation

pip install requests

## Setup

Get your API key from api-sports.io and pass it in:

## Quick Start

from football import Football

fb = Football("your_api_key")

teams = fb.get_teams(id=25)
leagues = fb.get_leagues(id=39)
