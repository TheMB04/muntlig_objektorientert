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
    navn = navn.replace("+", "")
    nanv = navn.replace("og", "")
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
            biler_sortert = reserve_liste[:]

            if min_pris.lower() == "ingen":
                ugyldig_min_pris = False

            else:
                try:
                    for bil in biler:
                        if lag_int(bil.return_pris()) < lag_int(min_pris):
                            biler_sortert.remove(bil)
                            
                    if lag_int(min_pris) < 0:
                        print("Ugyldig pris, vennligst prøv igjen")
                    elif len(biler_sortert) == 0:
                        print("Denne prisen gjør at det ikke er noen biler igjen i listen. Vennligst bruk en annen pris.")
                    else:
                        ugyldig_min_pris = False

                except:
                    print("Ugyldig input, prøv igjen")


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]

            
        while ugyldig_maks_pris:
            maks_pris = input("Hva er din ønsket makspris? (ingen/tall)")
            biler_sortert = reserve_liste[:]

            if maks_pris.lower() == "ingen":
                ugyldig_maks_pris = False

            else:
                try:
                    for bil in biler:
                        if lag_int(bil.return_pris()) > lag_int(maks_pris):
                            biler_sortert.remove(bil)
                    
                    if lag_int(maks_pris) < 0:
                        print("Ugyldig pris, vennligst prøv igjen")
                    elif len(biler_sortert) == 0:
                        print("Denne prisen gjør at det ikke er noen biler igjen i listen. Vennligst bruk en annen pris.")
                    else:
                        ugyldig_maks_pris = False

                except:
                    print("Ugyldig input, prøv igjen")


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_merke:
            onsket_merke = input("Hvilket bilmerke ser du etter? (ingen/BMW/Porsche/Chevrolet/Tesla/Bentley/Volvo/Land Rover/Kia/Mercedes-Benz/Hummer/Volkswagen/Toyota/Nissan/Audi/Ford/Peugeot/Opel/Saab)")
            biler_sortert = reserve_liste[:]
            
            if onsket_merke.lower() == "ingen":
                ugyldig_merke = False

            else:
                for bil in biler:
                    if simplifiser(onsket_merke) != simplifiser(bil.return_merke()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Enten så har vi ikke det merket, eller så samsvarer det ikke med tidligere søk, eller så har du skrevet feil. Vennligst prøv igjen.")
                else:
                    ugyldig_merke = False


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_modell:
            onsket_modell = input("Hvilken modell ser du etter? (ingen/modell)")
            biler_sortert = reserve_liste[:]
            
            if onsket_modell.lower() == "ingen":
                ugyldig_modell = False

            else:
                for bil in biler:
                    if simplifiser(onsket_modell) != simplifiser(bil.return_modell()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Enten så har vi ikke den modellen, eller så samsvarer den ikke med tidligere søk, eller så har du skrevet feil (kanskje har du skrevet en modell som ikke tilhører merket du ønsket?). Vennligst prøv igjen.")
                else:
                    ugyldig_modell = False


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_aarsmodell:
            onsket_aarsmodell = input("Hvilken årsmodell ser du etter? (ingen/årstall)")
            biler_sortert = reserve_liste[:]
            
            if onsket_aarsmodell.lower() == "ingen":
                ugyldig_aarsmodell = False

            else:
                for bil in biler:
                    if lag_int(onsket_aarsmodell) != lag_int(bil.return_aarsmodell()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Enten så har vi ikke den årsmodellen, eller så samsvarer den ikke med tidligere søk, eller så har du skrevet feil. Vennligst prøv igjen.")
                else:
                    ugyldig_aarsmodell = False


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_min_kilometer:
            min_kilometer = input("Hva er din ønsket minimums kjørelengde? (ingen/tall)")
            biler_sortert = reserve_liste[:]

            if min_kilometer.lower() == "ingen":
                ugyldig_min_kilometer = False

            else:
                try:
                    for bil in biler:
                        if lag_int(bil.return_kilometer()) < lag_int(min_kilometer):
                            biler_sortert.remove(bil)
                            
                    if lag_int(min_kilometer) < 0:
                        print("Ugyldig distanse, vennligst prøv igjen")
                    elif len(biler_sortert) == 0:
                        print("Denne distansen gjør at det ikke er noen biler igjen i listen. Vennligst bruk en annen distanse.")
                    else:
                        ugyldig_min_kilometer = False

                except:
                    print("Ugyldig input, prøv igjen")


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]

            
        while ugyldig_maks_kilometer:
            maks_kilometer = input("Hva er din ønsket maks kjørelengde? (ingen/tall)")
            biler_sortert = reserve_liste[:]

            if maks_kilometer.lower() == "ingen":
                ugyldig_maks_kilometer = False

            else:
                try:
                    for bil in biler:
                        if lag_int(bil.return_kilometer()) > lag_int(maks_kilometer):
                            biler_sortert.remove(bil)
                    
                    if lag_int(maks_kilometer) < 0:
                        print("Ugyldig distanse, vennligst prøv igjen")
                    elif len(biler_sortert) == 0:
                        print("Denne distansen gjør at det ikke er noen biler igjen i listen. Vennligst bruk en annen distanse.")
                    else:
                        ugyldig_maks_kilometer = False

                except:
                    print("Ugyldig input, prøv igjen")


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_gir:
            onsket_gir = input("Hvilket gir ser du etter? (ingen/automat/manuell)")
            biler_sortert = reserve_liste[:]
            
            if onsket_gir.lower() == "ingen":
                ugyldig_gir = False

            else:
                for bil in biler:
                    if simplifiser(onsket_gir) != simplifiser(bil.return_gir()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Enten så har ingen av bilene dette giret, eller så samsvarer den ikke med tidligere søk, eller så har du skrevet feil. Vennligst prøv igjen.")
                else:
                    ugyldig_gir = False


        reserve_liste = biler_sortert[:]
        biler = biler_sortert[:]


        while ugyldig_type:
            onsket_type = input("Hvilken type bil ser du etter? (ingen/diesel/bensin/elektrisk/el + bensin)")
            biler_sortert = reserve_liste[:]
            
            if onsket_type.lower() == "ingen":
                ugyldig_type = False

            else:
                for bil in biler:
                    if simplifiser(onsket_type) != simplifiser(bil.return_type()):
                        biler_sortert.remove(bil)
                
                if len(biler_sortert) == 0:
                    print("Enten så har vi ikke denne typen, eller så samsvarer den ikke med tidligere søk, eller så har du skrevet feil. Vennligst prøv igjen.")
                else:
                    ugyldig_type = False

        
        print('''
Her er alle bilene som passet dine ønsker, sortert etter pris: ''')

        ikke_riktig = False


    else:
        print("Ugyldig input, prøv igjen")


for bil in biler_sortert:
    print(bil.lag_oversikt())


