import states

def begin() :
    print("Je hebt besloten o te rennen")
    print("Je rent door het vuur en je hebt niks dat is mooi")
    print("Maar nu sta je voor een schuur met een kelder")
    print("Ga je de KELDER in of ga je de schuur in BRAND steken")
    antwoord = input("> ")
    if antwoord == "KELDER" :
        states.locatie = "KELDER"
    elif antwoord == "BRAND" :
        states.locatie = "BRAND"