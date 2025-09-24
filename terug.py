import states

def begin() :
    print("Je hoort een stem en die zegt als je weggaat vermoord ik je dus ga naar binnen")
    print("Ga e toch WEG of ga je naar het HUIS")
    antwoord = input("> ")
    if antwoord == "WEG" :
        states.locatie = "WEG"
    elif antwoord == "HUIS" :
        states.locatie = "HUIS"