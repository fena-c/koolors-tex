
from colorutils import Color, hex_to_hsv

import sys #.argv


print(sys.argv)
en_hex = str(sys.argv[1])

en_hsv = hex_to_hsv(en_hex)




colores = []

for i in range(5):
    color = Color(hsv = (((en_hsv[0] + 72*i)% 360), .2, .85))
    shadow = Color(hsv = (((en_hsv[0] + 72*i)% 360), .2, .70))
    colores.append([color, shadow])


bg = Color(hsv = (en_hsv[0], 0.02, .95))
bg2 = Color(hsv = (en_hsv[0], 0.02, .95))


archivo = open("koolors.sty", "w")



for i in range(5):
    print(r"\definecolor{color" + f"{i+1}" + r"}{HTML}{" + colores[i][0].hex[1:] + r"}", file = archivo)
    print(r"\definecolor{color" + f"{i+1}2" + r"}{HTML}{" + colores[i][1].hex[1:] + r"}", file = archivo)

print(r"\definecolor{bg}{HTML}{" + bg.hex[1:] + r"}", file = archivo)
print(r"\definecolor{bg2}{HTML}{" + bg2.hex[1:] + r"}", file = archivo)

archivo.close()




