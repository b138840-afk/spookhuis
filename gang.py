import states

def begin():
    print("je staat in de gang voor een TRAP.")
    print("kies je voor de TRAP of ga je TERUG?")
    antwoord = input(">")
    if antwoord == "TRAP" :
        states.locatie = "ZOLDER"
    elif antwoord == "TERUG" :
        states.locatie = "HUIS"
        
    