import states

def begin() :
    print("Je gaat de trap af de kelder in achterin zit iemand vast geketend")
    print("Ga je haar BEVRIJDEN of ga je terug en de schuur alsnog in BRAND steken")
    antwoord = input("> ")
    if antwoord == "BEVRIJDEN" :
        states.locatie = "BEVRIJDEN"
    elif antwoord == "BRAND" :
        states.locatie = "BRAND"