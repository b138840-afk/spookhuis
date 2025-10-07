import states
import terug
import weg
import huis
import zolder
import raam
import dakgoot
import onderzoek
import tuin
import emmer
import zitten
import ren
import kelder
import brand
import gang

while True :
    if states.locatie == "TERUG" :
        terug.begin()
    elif states.locatie == "WEG" :
        weg.begin() 
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
    elif states.locatie == "EMMER" :
        emmer.begin()
    elif states.locatie == "ZITTEN" :
        zitten.begin()
    elif states.locatie == "REN" :
        ren.begin()
    elif states.locatie == "KELDER" :
        kelder.begin()
    elif states.locatie == "BRAND" :
        brand.begin()
    elif states.locatie == "GANG" :
        gang.begin()