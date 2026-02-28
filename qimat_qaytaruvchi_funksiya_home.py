def foydalanuvchi_yarat():
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    tugilgan_yil = int(input("Tug'ilgan yil: "))
    tugilgan_joy = input("Tug'ilgan joy: ")
    hozirgi_yil = int(input("Hozirgi yil: "))

    email = input("Email (ixtiyoriy, bo'sh qoldirish mumkin): ")
    telefon = input("Telefon (ixtiyoriy, bo'sh qoldirish mumkin): ")

    yosh = hozirgi_yil - tugilgan_yil

    foydalanuvchi = {
        "ism": ism,
        "familiya": familiya,
        "tugilgan_yil": tugilgan_yil,
        "tugilgan_joy": tugilgan_joy,
        "yosh": yosh
    }

    if email != "":
        foydalanuvchi["email"] = email

    if telefon != "":
        foydalanuvchi["telefon"] = telefon

    return foydalanuvchi


user = foydalanuvchi_yarat()
print(user)





mijozlar=[]
while True:
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    tugilgan_yil = int(input("Tugilgan yil: "))
    tugilgan_joy = input("Tugilgan joy: ")
    hozirgi_yil = int(input("Hozirgi yil: "))
    yosh = hozirgi_yil - tugilgan_yil
    mijozlar.append((ism, familiya, tugilgan_yil, tugilgan_joy, hozirgi_yil, yosh))
    qoshish = input("Yana kiritasizmi: ")
    if qoshish.lower()=="no":
        break
print(mijozlar)



def kattasini_aniqlovchi():
    """Uchta sondan kattasini aniqlovchi"""
    a=int(input("1-sonni kiriting: "))
    b=int(input("2-sonni kiriting: "))
    c=int(input("3-sonni kiriting: "))
    d=max(a,b,c)
    print("Kattasi",d)

kattasini_aniqlovchi()




def aylana(radius):
    return {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * 3.14 * radius,
        "yuza": 3.14 * radius ** 2
    }

r = float(input("Radiusni kiriting: "))
print(aylana(r))


def tub_aniqlovchi():
    """Tub aniqlovchi"""
    for i in range(2,100):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
tub_aniqlovchi()


n = int(input("Nechta son kerak: "))

a, b = 1, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b