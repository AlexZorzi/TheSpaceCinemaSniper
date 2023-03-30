import re
import json
import requests
from Film import Film


class SpaceCinema:
    BASE = "https://www.thespacecinema.it"
    LOGIN = BASE + "/security/loginajax"
    FILMBYCINEMA = BASE + "/data/filmswithshowings/"
    SEATINGDATA = BASE + "/data/SeatingData"

    def __init__(self, username, password, debug=False):
        self.SESSION = requests.session()
        self.cinemas = {}
        self.films = []
        self.username = username
        self.password = password
        self.DEBUG = debug

    def login(self):
        r = self.SESSION.post(self.LOGIN, data={"type": "email", "email": self.username, "password": self.password})
        if r.json()["data"]["logged"]:
            print("Logged In!")
        else:
            print("Error Login! exiting...")
            exit(1)

    def loadAvailCinemas(self):
        homepage = self.SESSION.get(self.BASE).text
        result = re.search('var vueLangsAndCinemas = (.*) ;', homepage)
        parsed = json.loads(result.group(1))
        for cinema in parsed["cinemas"]["whatsOnCinemas"]:
            self.cinemas[cinema["CinemaId"]] = cinema["CinemaName"]
        print("Loaded Cinemas!")
        if self.DEBUG:
            print(self.cinemas)

    def loadfilmlistbyCinema(self, cinema_id):
        data = self.SESSION.get(self.FILMBYCINEMA + cinema_id).json()
        for film_data in data["films"]:
            self.films.append(Film(film_data))

    def getSeatingData(self, Time, CinemaID):
        link = Time.getLink().split("/")
        payload = {"cinemaId" : CinemaID, "filmId" : link[4], "filmSessionId" : link[6], "userSessionId" : self.SESSION.cookies.get('UserSessionId')}
        data = self.SESSION.post(self.SEATINGDATA, data=payload, cookies={'cf_clearance': 'uKa.paKuQwd3pC.X5vkAr7roZI1zWFXwNM2k_jBAE0w-1680216250-0-250'})
        print()