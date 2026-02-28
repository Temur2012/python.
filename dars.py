# shahar = "Urganch"
# viloyat = 'Xorazm'
# print(shahar, viloyat)
#
# matn = "Men yangi 💻ć oldim"
# print(matn)
#
# ism = 'Jonibek'
# # ism =5
# print("Mening ismim " + ism)
#
# ism = 'Jonibek'
# familiya = ' Uralov'
# print(ism + familiya)
#
# ism = "Jonibek"
# familiya = 'Uralov'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)
#
# ism = "Jonibek"
# familiya = 'Uralov'
# print(f"Salom, mening ismim {ism} {familiya}!")
#
# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')
#
# ism = 'jonibek'
# familiya = 'uralov'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())
#
# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")
#
# ism = input("Ismingiz nima?\n")
# print("Assalom alaykum, " + ism.title())

# son = input("Son kiriting: ")
# print(float(son)+2)


# a = 20  # Sonlar musbat yoki
# b = -30 # manfiy bo'lishi mumkin
# c = a + b
# print(c)
#
# # Kvadratning yuzini hisoblaymiz
# kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
# kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
# print(kvdrt_yuzi)
#
# a = -20
# b = 40
# c = b/a
# print(c) # natija o'nlik son bo'ladi
#
# aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shunday yozdik
# print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")
#
# x, y, z = 10, -7.25, -30
# print(x, y, z)

# typecasting
# a = 10
# print(a)
# print(type(a))
#
# a = float(a)
# print(a)
#
# a = str(a)
# print(a)
# print(type(a))
#
# b = "102"
# print(b)
# print(type(b))
#
# b = float(b)
# print(b)
#
# b = int(b)
# print(b)

#foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil =input("Tug'ilgan yilingizni kiriting: ")
# #foydalanuvchi yoshini xisoblaymiz
# yosh = 2026 - int(t_yil) #
# #foydalanuvchi yoshini konsolga chiqaramiz
# # print("Siz " + str(yosh) + " yoshda ekansiz")
# print(f"siz {yosh} dasiz")

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat
print(mevalar)
print(narhlar)
print(sonlar)
print(ismlar)
print(mevalar[0])


print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])


print(narhlar[2] + narhlar[3])

narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
print(mevalar)

cars = [] # bo'sh ro'yxat yaratamiz
cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
print(cars)

cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
print(cars)
cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
print(cars)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
print(mevalar)

hayvonlar = ['it', 'mushuk', 'sigir', 'qoy', 'quyon', 'mushuk']
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi

print(hayvonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)