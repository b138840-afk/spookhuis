import states

def begin() :
    print("Je hebt dus besloten om onderzoek te doen alleen hier is niks te vinden")
    print("Dus ga je naar het RAAM of ga je uit het HUIS")
    antwoord = input("> ")
    if antwoord == "RAAM" :
        states.locatie = "RAAM"
    elif antwoord == "HUIS" :
        states.locatie = "HUIS"