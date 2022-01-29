import numpy
import json

with open("config.json") as j:
    js = json.load(j)
print(js)
print(type(js[0]['NFRM']))
for x in range(0, js[0]['NFRM']):
    y = js[0]['FLEN']/((2*numpy.pi)*(js[0]['FRAO'] + (x * js[0]['FTHN'])))
    print(str(str(x) + " :: " + str(y)))

