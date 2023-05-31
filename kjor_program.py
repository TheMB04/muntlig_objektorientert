import json
from bil import Bil

fil = open("muntlig_objektorientert/biler.json", encoding = "utf-8")
data = json.load(fil)
fil.close()

biler = []

def lag_int(pris):
    pris = pris.replace(" ", "")
    pris = pris.replace("kr", "")
    return int(pris)

for i in data:
    bil = Bil(i["merke"], i["modell"], i["aarsmodell"], i["kilometer"], i["gir"], i["type"], i["pris"], i["url"])
    biler.append(bil)

biler_sortert = sorted(biler, key=lambda bil: lag_int(bil._pris))

for bil in biler_sortert:
    print(bil._pris)


