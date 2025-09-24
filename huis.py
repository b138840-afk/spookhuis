import states


def begin() :
    print("je staat in een tuin voor een huis met een deur")
    print("kies je voor de DEUR binnen te gaan of ga je TERUG")
    antwoord = input(">")
    if antwoord == "DEUR" :
        states.locatie = "GANG"
    elif antwoord == "TERUG" :
        states.locatie = "HUIS"