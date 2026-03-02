# import modul as avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz
#
# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)
#
# from modul import avto_info, info_print
# avto1=avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)
#
# from modul import avto_info as ai, info_print as pi
# avto1=ai("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# print(avto1)
#
# from modul import *
# avto1=info_print("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)



import math
x=400
print(math.sqrt(x))

print(pow(5,2))

from math import pi
print(pi)

print(math.log2(8))

print(math.log10(x))

print(math.ceil(x))

import random as r
son=r.randint(0,100)
print(son)

ismlar=['olim','anvar','hasan','husan']
ism=r.choice(ismlar)
print(ism)
print(r.choice(ism))

x=list(range(0,51,5))
print(x)
print(r.choice(x))

x=list(range(11))
print(x)
r.shuffle(x)
print(x)
