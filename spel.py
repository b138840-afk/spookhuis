import states
import terug
import weg
import huis
import zolder
import raam
# import dakgoot
import onderzoek
# import tuin
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
#     elif states.locatie == "DAKGOOT" :
#       dakgoot.begin()
    elif states.locatie == "ONDERZOEK" :
         onderzoek.begin()
#     elif states.locatie == "TUIN" :
#          tuin.begin()
    elif states.locatie == "GANG" :
        gang.begin()