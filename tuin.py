import states

def begin() :
    print("Je staat in de tuin aleen je bent omringt met vuur wat ga je doen")
    print("Naast je staat een emmer met water")
    print("pak je de EMMER met water,ga je ZITTEN of REN je door het vuur")
    antwoord = input("> ")
    if antwoord == "EMMER" :
        emmer()
    elif antwoord == "ZITTEN" :
        states.locatie = "ZITTEN"
    elif antwoord == "REN" :
        states.locatie = "REN"
        
def emmer() :        
    print("Je pakt de emmer en gooit het over het vuur, maar in plaats van dat er water in zit zit er benzine in.")
    print("Hierdoor verbrandt je levent en ga je dood")
    print("GAME OVER!!!!!!!!!!!!!!!")
    states.locatie = "END"
    
def zitten() :
    print("Je hebt dus besloten om te gaan ziiten in de kring van vuur")
    print("Alleen dit gaat niet het vuur is zo het dat je gelijk brandwonden krijgt en hier sterf je aan.")
    print("GAME OVER!!!!!!!!!!!")
    states.locatie = "END"
