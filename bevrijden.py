import states

def begin() :
    print("Je bevrijdt het meisje en voor je zie je een tunnel")
    print("Ga JIJ als eerst of laat je het MEISJE als eerst de tunnel in gaan")
    antwoord = input ("> ")
    if antwoord == "JIJ" :
        states.locatie = "JIJ"
    elif antwoord == "MEISJE" :
        states.locatie = "MEISJE"