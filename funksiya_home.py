def yosh_aniqlovchi(tugilgan_yili,hozirgi_yil=2026):
    """Yosh aniqlovchi"""
    print(hozirgi_yil-tugilgan_yili)
tugilgan_yili=int(input("Yoshni kiriting"))
yosh_aniqlovchi(tugilgan_yili)



def kub_va_kvadrat_aniqlovchi(son):
    """kub va kvadrat aniqlovchi"""
    print(f"Kub {son**3} , Kvadrat {son**2}")
son=int(input("Sonni kiriting"))
kub_va_kvadrat_aniqlovchi(son)


def juft_yoki_toq(son):
    """Juft yoki toqlikini aniqlab beradi"""
    if son % 2 != 0:
        print("Toq son")
    elif son % 2 == 0:
        print("Juft son")
son=int(input("Sonni kiriting:"))
juft_yoki_toq(son)


def katta_yoki_teng(son,son1):
    """Katta yoki tengliki aniqlab beradi """
    if son==son1:
        print("Teng")
    elif son>son1:
        print("1-son katta")
    else:
        print("2-son katta")
son=int(input("1-sonni kiriting:"))
son1=int(input("2-sonni kiriting:"))
katta_yoki_teng(son,son1)



def daraja(x,y):
    """X ni Y darajasi"""
    print(x**y)
x=int(input("X-kiriting:"))
y=int(input("Y-kiriting:"))
daraja(x,y)



def daraja(x,y=2):
    """X ni 2-darajasi"""
    print(x**y)
x=int(input("X-kiriting:"))
daraja(x)



def bolish(son):
    for i in range(2,11):
        if son % i==0:
            print(f"{son} {i} ga bo'linadi")
son=int(input("Son kiriting:"))
bolish(son)