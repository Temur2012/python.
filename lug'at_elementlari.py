talaba_0={
    'ism':'jonibek',
    'familya':'uralov',
    'yosh':22,
    'fakultet':'komputer injenering',
    'kurs':2
}
print(talaba_0.items())

for kalit, qiymat in talaba_0.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat}\n")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }


for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")


mahsulotlar= { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000,
}

print(mahsulotlar.keys())

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())


bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")


for buyum in mahsulotlar:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'konga {buyum} ham olib keling")


print("Do'kondagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())


print(telefonlar.values())
print('Foydalanuvchi quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }
print('Foydalanuvchilar quyidagi telefonlarni ishlatshdi:')
for tel in telefonlar.values():
    print(tel)


print('Foydalanuvchilar quyidagi telefonlarni ishlatishdi:')
for tel in set(telefonlar.values()):
    print(tel)