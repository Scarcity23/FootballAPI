import time
import requests

class APIWrapper:
    def __init__(self, api_key: str):
        self.headers = {'x-apisports-key': api_key}
        self.base_url = "https://v3.football.api-sports.io"

    def get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}{endpoint}"
        delay = 1
        for attempt in range(8):
            try:
                response = requests.get(url, headers=self.headers, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:  # rate limited
                    time.sleep(delay)
                    delay *= 2
                else:
                    print(f"HTTP error: {e}")
                    return None
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                return None
        print("Max retries exceeded")
        return None