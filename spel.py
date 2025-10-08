import states
import terug
import huis
import zolder
import raam
import dakgoot
import onderzoek
import tuin
import ren
import kelder
import brand
import bevrijden
import jij
import meisje
import gang

while True :
    if states.locatie == "TERUG" :
        terug.begin()
    elif states.locatie == "HUIS" :
        huis.begin()
    elif states.locatie == "ZOLDER" :
        zolder.begin()
    elif states.locatie == "RAAM" :
        raam.begin()
    elif states.locatie == "DAKGOOT" :
        dakgoot.begin()
    elif states.locatie == "ONDERZOEK" :
        onderzoek.begin()
    elif states.locatie == "TUIN" :
        tuin.begin()
    elif states.locatie == "REN" :
        ren.begin()
    elif states.locatie == "KELDER" :
        kelder.begin()
    elif states.locatie == "BRAND" :
        brand.begin()
    elif states.locatie == "BEVRIJDEN" :
        bevrijden.begin()
    elif states.locatie == "JIJ" :
        jij.begin()
    elif states.locatie == "MEISJE" :
        meisje.begin
    elif states.locatie == "GANG" :
        gang.begin()
    else :
        print("Game won")