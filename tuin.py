import states

def begin() :
    print("Je staat in de tuin aleen je bent omringt met vuur wat ga je doen")
    print("Naast je staat een emmer met water")
    print("pak je de EMMER met water,ga je ZITTEN of REN je door het vuur")
    antwoord = input("> ")
    if antwoord == "EMMER" :
        states.locatie = "EMMER"
    elif antwoord == "ZITTEN" :
        states.locatie = "ZITTEN"
    elif antwoord == "REN" :
        states.locatie = "REN"