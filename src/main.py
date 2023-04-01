from SpaceCinema import SpaceCinema

# Demo Work in progress

def main():
    #username = input("username: ")
    #password = input("password: ")
    sc = SpaceCinema("", "", debug=False)
    sc.login()
    sc.loadAvailCinemas()

    print("seleziona un cinema:")
    i = 0
    for cinema in sc.cinemas.keys():
        print(cinema+") "+sc.cinemas[cinema])
        i +=1
    cinema_selected = "23" #input("cinema: ")
    sc.loadfilmlistbyCinema(cinema_selected)

    print("seleziona un film:")
    filmn = 0
    for film in sc.films:
        print(str(filmn)+") "+ film.title)
        filmn += 1
    film_selected = 0 #int(input("film: "))

    print("seleziona un giorno:")
    giornon = 0
    for giorno in sc.films[film_selected].showings:
        print(str(giornon) + ") " + giorno.date_long)
        giornon += 1
    giorno_selected = 0 #int(input("giorno: "))

    print("seleziona un orario:")
    orarion = 0
    for orario in sc.films[film_selected].showings[giorno_selected].times:
        print(str(orarion) + ") " + orario.time + " sala "+orario.screen_number)
        orarion += 1
    orario_selected = 0 #int(input("orario: "))

    #print(sc.BASE + sc.films[film_selected].showings[giorno_selected].times[orario_selected].getLink())
    seating = sc.getSeatingData(sc.films[film_selected].showings[giorno_selected].times[orario_selected], cinema_selected)
    seating.selectBestSeatsByN(3)

if __name__ == '__main__':
    main()
