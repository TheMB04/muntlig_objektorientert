import json
from bil import Bil

fil = open("muntlig_objektorientert/biler.json", encoding = "utf-8")
data = json.load(fil)
fil.close()

biler = []

ikke_riktig = True
ugyldig_min_pris = True
ugyldig_maks_pris = True


def lag_int(pris):
    pris = pris.replace(" ", "")
    pris = pris.replace("kr", "")
    return int(pris)


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
        while ugyldig_min_pris:
            min_pris = input("Hva er din ønsket minimumspris? (ingen/tall)")

            if min_pris.lower() == "ingen":
                ugyldig_min_pris = False
            else:
                try:
                    min_pris = min_pris.replace(" ", "")
                    min_pris = int(min_pris.replace("kr", ""))

                    for bil in biler:
                        if lag_int(bil.return_pris()) < min_pris:
                            biler_sortert.remove(bil)
                            
                    ugyldig_min_pris = False
                except:
                    print("Ugyldig input, prøv igjen")

            
        while ugyldig_maks_pris:
            maks_pris = input("Hva er din ønsket minimumspris? (ingen/tall)")

            if min_pris.lower() == "ingen":
                ugyldig_maks_pris = False
            else:
                try:
                    maks_pris = maks_pris.replace(" ", "")
                    maks_pris = int(maks_pris.replace("kr", ""))

                    for bil in biler:
                        if lag_int(bil.return_pris()) > maks_pris:
                            biler_sortert.remove(bil)
                            
                    ugyldig_maks_pris = False
                except:
                    print("Ugyldig input, prøv igjen")
            
        
        print('''
Her er alle bilene som passet dine ønsker, sortert etter pris: ''')
        ikke_riktig = False

    else:
        print("Beklager det forstod jeg ikke, prøv igjen")


for bil in biler_sortert:
    print(bil.lag_oversikt())


