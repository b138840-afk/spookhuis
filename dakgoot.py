import states

def begin() :
    print("Je staat in de dakgoot voor je zie je een kring met vuur in de tuin")
    print("Spring je de TUIN in of ga je toch, maar ONDERZOEK doen")
    antwoord = input("> ")
    if antwoord == "TUIN" :
        states.locatie = "TUIN"
    elif antwoord == "ONDERZOEK" :
        states.locatie = "ONDERZOEK"