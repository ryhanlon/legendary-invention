"""
This file was written Rebecca Hanlon.

"""


class RainStation:
    def __init__(self, name: str, address: str, url: str):
        self.name = name
        self.address = address
        self.url = url
        self.rain_data = list()

        self.raw_text = self.scrape_station()

    def scrape_station(self):
        response = requests.get(self.url)
        raw_text = response.text
        return raw_text

    def max_day(self):
        number_cruncher()
        pass

    def max_year(self):
        pass

    def summary(self):
        pass

    def parse_header(self):
        name, address
        pass

    def __repr__(self):
        message = "RainStation(name={}, address={}, url={}".format(self.name, self.address, self.url)
        return message

    def __str__(self):
        message = "This is the station {}, {}.".format(self.name, self.address)
        return message




def compile_links():
    BASE_URL = "https://or.water.usgs.gov/precip/"

    response = requests.get(BASE_URL)
    raw = response.text
    soup = BeautifulSoup(raw, 'html.parser') for link


def run_links():
    links = complile_links

    rain_stations = list()
    for link in links:
        rs = RainStation(url=link)

if __name__ = '__main__'
    run-links()