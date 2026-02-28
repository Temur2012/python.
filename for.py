# 1
pochta = ["q1w2@gmail.com", "q1w2yahoo.com", "q1w2@outlook.com"]
for email in pochta:
    if email.endswith("@gmail.com") or email.endswith("yahoo.com") or email.endswith("@outlook.com"):
        print(email, "Email to‘g‘ri")
else:
    print(email, "Email noto‘g‘ri")

#2
 parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
 for parol in parollar:
     raqam_soni = 0
     for belgi in parol:
         if belgi.isdigit():
             raqam_soni += 1
     if len(parol) < 8:
         print(parol, "- Juda qisqa")
     elif raqam_soni == 0:
          print(parol, "- Kuchsiz parol")
     else:
         print(parol, "- Kuchli parol")


# 3
 havo = [20, 22, 19, 24, 25, 23, 21]
 for havo1 in havo:
     if havo1 > 22:
         print(havo1, "Iliq kun")
     else:
         print(havo1, "Salqin kun")


# 4
 taomlar = ["Osh", "Shashlik", "Manti", "Lag’mon"]

 buyurtma = input("Buyurtmani kiriting: ")

 if buyurtma in taomlar:
     print("Buyurtma qabul qilindi")
 else:
     print("Kechirasiz, bunday taom yo'q")



# 5
 yosh=int(input("Yoshingizni kiriting:"))
 if yosh>18:
     print("Xush kelibsiz:")
 else:
     print("Yosh chegarasiga yetmaydi:")


# 6
 xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
 for xabarlar1 in xabarlar:
     if xabarlar== "Batareya past":
         print("Telefoningizni quvvatlan")



# 7
 fayllar = ["kitob.jpg", "ko_ jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
 rasmlar=[]
 musiqalar=[]
 for fayl in fayllar:
     if fayl.find(".jpg") !=-1:
         rasmlar.append(fayl)
     elif fayl.find(".mp3") !=-1:
         musiqalar.append(fayl)

 print("Rasmlar:", rasmlar)
 print("Musiqalar:", musiqalar)