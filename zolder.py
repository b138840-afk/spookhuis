import states

def begin() :
    print("Je staat op de zolder van het huis")
    print("Ga je naar het RAAM of blijf je ga je ONDERZOEK doen op de zolder")
    antwoord = input("> ")
    if antwoord == "RAAM" :
        states.locatie = "RAAM"
    elif antwoord == "ONDERZOEK" :
        states.locatie = "ONDERZOEK"