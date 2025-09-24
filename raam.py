import states

def begin() :
    print("Je staat voor een raam")
    print("Ga je door het raam de DAKGOOT op of ga je toch ONDERZOEK doen")
    antwoord = input("> ")
    if antwoord == "DAKGOOT" :
        states.locatie = "DAKGOOT" 
    elif antwoord == "ONDERZOEK" :
        states.locatie = "ONDERZOEK" 