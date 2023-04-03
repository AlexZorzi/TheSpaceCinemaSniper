import json
from SpaceCinema import SpaceCinema
from selenium import webdriver


# Demo Work in progress

def main():
    f = open("credentials.json")
    cred = json.load(f)
    sc = SpaceCinema(cred["user"], cred["password"], debug=False)
    sc.login()
    sc.loadAvailCinemas()

    print("seleziona un cinema:")
    i = 0
    for cinema in sc.cinemas.keys():
        print(cinema+") "+sc.cinemas[cinema])
        i +=1
    cinema_selected = input("cinema: ")
    sc.loadfilmlistbyCinema(cinema_selected)

    print("seleziona un film:")
    filmn = 0
    for film in sc.films:
        print(str(filmn)+") "+ film.title)
        filmn += 1
    film_selected = int(input("film: "))

    print("seleziona un giorno:")
    giornon = 0
    showings = sc.films[film_selected].showings
    for giorno in showings:
        print(str(giornon) + ") " + giorno.date_long)
        giornon += 1
    giorno_selected = int(input("giorno: "))

    print("seleziona un orario:")
    orarion = 0
    giorno_data = showings[giorno_selected]
    for orario in giorno_data.times:
        print(str(orarion) + ") " + orario.time + " sala "+orario.screen_number)
        orarion += 1
    orario_selected = int(input("orario: "))
    orario_data = giorno_data.times[orario_selected]

    seating = sc.getSeatingData(orario_data, cinema_selected)

    seats_number = int(input("Quante persone? :"))
    sc.checkoutSeats(orario_data, seating.selectBestSeatsByN(seats_number), cinema_selected)

    a = sc.SESSION.cookies.get_dict()
    browser = webdriver.Chrome()
    browser.get("https://www.thespacecinema.it")
    for cookie in a.keys():
        browser.delete_cookie(cookie)
        browser.add_cookie({"name":cookie,"value":a[cookie], "domain":"thespacecinema.it", "path":"/"})
    browser.get("https://www.thespacecinema.it/prenotare-il-biglietto/review/"+cinema_selected+"/"+sc.getFilmidBySeating(sc.films[film_selected].showings[giorno_selected].times[orario_selected])+"/"+sc.getFilmSessionidBySeating(sc.films[film_selected].showings[giorno_selected].times[orario_selected]))
    print("https://www.thespacecinema.it/prenotare-il-biglietto/review/"+cinema_selected+"/"+sc.getFilmidBySeating(sc.films[film_selected].showings[giorno_selected].times[orario_selected])+"/"+sc.getFilmSessionidBySeating(sc.films[film_selected].showings[giorno_selected].times[orario_selected]))
    while (True):
        pass

if __name__ == '__main__':
    main()
