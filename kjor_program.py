import json
from bil import Bil

fil = open("muntlig_objektorientert/biler.json", encoding = "utf-8")
data = json.load(fil)
fil.close()

biler = []

ikke_riktig = True
ugyldig_min_pris = True
ugyldig_maks_pris = True
ugyldig_merke = True
ugyldig_modell = True
ugyldig_aarsmodell = True
ugyldig_min_kilometer = True
ugyldig_maks_kilometer = True
ugyldig_gir = True
ugyldig_type = True


def lag_int(pris):
    pris = pris.replace(" ", "")
    pris = pris.replace("kr", "")
    pris = pris.replace("km", "")
    return int(pris)

def simplifiser(navn):
    navn = navn.replace(" ", "")
    navn = navn.replace("-", "")
    return navn.lower()

for i in data:
    bil = Bil(i["merke"], i["modell"], i["aarsmodell"], i["kilometer"], i["gir"], i["type"], i["pris"], i["url"])
    biler.append(bil)

biler_sortert = sorted(biler, key=lambda bil: lag_int(bil.return_pris()))


while ikke_riktig:
    start = input("Hei, vil du sortere ut i fra egne ønsker? (ja/nei)")


    if start.lower() == "nei":
        print('''
Den er grei, her er alle bilene på markedet, sortert etter pris: ''')
        ikke_riktig = False


    
    elif start.lower() == "ja":
        reserve_liste = biler_sortert[:]

        while ugyldig_min_pris:
            min_pris = input("Hva er din ønsket minimumspris? (ingen/tall)")

            if min_pris.lower() == "ingen":
                ugyldig_min_pris = False

            else:
                biler_sortert = reserve_liste[:]

                try:
                    min_pris = min_pris.replace(" ", "")
                    min_pris = int(min_pris.replace("kr", ""))

                    for bil in biler:
                        if lag_int(bil.return_pris()) < min_pris:
                            biler_sortert.remove(bil)
                            
                    ugyldig_min_pris = False

                except:
                    print("Ugyldig input, prøv igjen")


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]

            
        while ugyldig_maks_pris:
            maks_pris = input("Hva er din ønsket makspris? (ingen/tall)")

            if maks_pris.lower() == "ingen":
                ugyldig_maks_pris = False

            else:
                biler_sortert = reserve_liste[:]

                try:
                    maks_pris = maks_pris.replace(" ", "")
                    maks_pris = int(maks_pris.replace("kr", ""))

                    for bil in biler:
                        if lag_int(bil.return_pris()) > maks_pris:
                            biler_sortert.remove(bil)
                    
                    if len(biler_sortert) == 0:
                        print("Denne prisen")
                    else:
                        
                        ugyldig_maks_pris = False

                except:
                    print("Ugyldig input, prøv igjen")



        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_merke:
            onsket_merke = input("Hvilket bilmerke ser du etter? (ingen/BMW/Porsche/Chevrolet/Tesla/Bentley/Volvo/Land Rover/Kia/Mercedes-Benz/Hummer/Volkswagen/Toyota/Nissan/Audi/Ford/Peugeot/Opel/Saab)")
            
            if onsket_merke.lower() == "ingen":
                ugyldig_merke = False
            else:
                biler_sortert = reserve_liste[:]

                for bil in biler:
                    if simplifiser(onsket_merke) != simplifiser(bil.return_merke()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Det merket har vi ikke, eller så har du skrevet feil. Vennligst prøv igjen.")
                else:
                    ugyldig_merke = False


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_modell:
            onsket_modell = input("Hvilken modell ser du etter? (ingen/modell)")
            
            if onsket_modell.lower() == "ingen":
                ugyldig_modell = False
            else:
                biler_sortert = reserve_liste[:]

                for bil in biler:
                    if simplifiser(onsket_modell) != simplifiser(bil.return_modell()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Den modellen har vi ikke, eller så har du skrevet feil (kanskje har du skrevet en modell som ikke tilhører merket du ønsket?). Vennligst prøv igjen.")
                else:
                    ugyldig_modell = False


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_aarsmodell:
            onsket_aarsmodell = input("Hvilken årsmodell ser du etter? (ingen/årstall)")
            
            if onsket_aarsmodell.lower() == "ingen":
                ugyldig_aarsmodell = False
            else:
                biler_sortert = reserve_liste[:]

                for bil in biler:
                    if lag_int(onsket_aarsmodell) != lag_int(bil.return_modell()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Den årsmodellen har vi ikke, eller så har du skrevet feil. Vennligst prøv igjen.")
                else:
                    ugyldig_aarsmodell = False

        

        
        print('''
Her er alle bilene som passet dine ønsker, sortert etter pris: ''')

        ikke_riktig = False


    else:
        print("Ugyldig input, prøv igjen")


for bil in biler_sortert:
    print(bil.lag_oversikt())


