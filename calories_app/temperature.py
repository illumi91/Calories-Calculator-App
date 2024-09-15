import requests
from selectorlib import Extractor
from pathlib import Path

class Temperature:
    """
    Represents a temperature value extracted from the timeanddate.com/weather webpage.
    """

    base_url = "https://www.timeanddate.com/weather/"
    directory_name = Path("calories_app")
    extractor_yaml = directory_name.joinpath("temperature.yaml")

    def __init__(self, country, city):
        self.country = country.lower()
        self.city = city.lower().replace(" ", "-")

    def _build_url(self):
        return f"{self.base_url}{self.country}/{self.city}"

    def _scrape_temperature(self):
        headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
        request = requests.get(self._build_url(), headers=headers)
        extractor = Extractor.from_yaml_file(self.extractor_yaml)

        return extractor.extract(request.text)["temp"]

    def get(self):
        temperature = float(self._scrape_temperature().replace('\xa0°C', '').strip())

        return temperature

