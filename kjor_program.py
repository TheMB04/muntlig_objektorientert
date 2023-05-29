import json
from bil import Bil

fil = open("muntlig_objektorientert/biler.json", encoding = "utf-8")
data = json.load(fil)
fil.close()

biler = []

for i in data:
    bil = Bil(i["merke"], i["modell"], i["aarsmodell"], i["kilometer"], i["gir"], i["type"], i["pris"], i["url"])
    biler.append(bil)

print(biler[0].return_merke())