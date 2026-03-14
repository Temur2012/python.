# import math
# uzunlik= lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
#
#
# product=lambda x,y: x**y
# print(product(3,2))
#
#
# def daraja(n):
#     return lambda x: x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")


from math import sqrt

from dars import mevalar

sonlar=list(range(11))
ildizlar=list(map(sqrt,sonlar))
print(ildizlar)


sonlar=list(range(11))

def darja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x
print(list(map(darja2,sonlar)))


kvadratlar=list(map(lambda x: x*x,sonlar))
print(kvadratlar)


kvadratlar=[]
for son in sonlar:
    kvadratlar.append(son)



ismlar=['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))



import random as r
sonlar= r.sample(range(100),10)
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0
juft_sonlar=list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)


import random as r
sonlar = r.sample(range(100),10)
juft_sonlar=list(filter(lambda son : son%2==0 ,sonlar))

print(sonlar)
print(juft_sonlar)

mevalar=['olma','anor','anjir','shaftoli',"o'rik",'tarvuz','qovun','banan']

mevalar_b=list(filter(lambda meva : meva.strartwith('b') ,mevalar))
print(mevalar_b)


mevalar2=list(filter(lambda meva:len(meva)<=5 ,mevalar))
print(mevalar2)