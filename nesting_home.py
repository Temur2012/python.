malumot = {
    'Abu': [":Abu Ali ibn Sino (Avitsenna) – buyuk tabib va faylasuf."],
    'Beruniy': [":Abu Rayhon Beruniy(973–1048) – Qomusiy olim."],
    'Xorazmiy': [":Al-Xorazmiy(taxminan 783–850) – Algebra asoschisi."],
    'Imom': [":Imom Buxoriy(810–870) – Hadis ilmi olimi."]
}

for ism, malumotlar in malumot.items():
    print(f"\n{ism.title()}", end='')
    for mal in malumotlar:
        print(f'{mal.upper()} ', end='')

asarlar = {
    'Abu': ["\n Al-Qonun fi’t-tibb\n", "Kitob ash-shifo\n", "Donishnoma\n", "Kitob an-najot\n"],
    'Beruniy': ["\n Hindiston\n", "Geodeziya\n", "Mineralogiya\n", "Saydana\n"],
    'Xorazmiy': ["\n Al-kitob al-muxtasar fi hisob al-jabr val-muqobala\n", "Zij al-Sindhind\n", "Kitob surat al-ard\n",
                 "Hisob al-hind\n"],
    'Imom': ["\n Al-jome’ as-sahih\n", "Al-adab al-mufrad\n", "At-tarix al-kabir\n", "At-tarix as-sag‘ir"]

}
for ism, asarlar in asarlar.items():
    print(f"\n{ism.title()}", end='')
    for mal in asarlar:
        print(f'{mal.upper()} ', end='')


kinolar = {
    'Alisher': ["\n Terminator\n", "Ramboo\n", "Titanic\n"],
    'Vali': ["\n Tenet\n", "Inseption\n", "Interstellar\n"],
    'Hasan': ["\n Abdullajon\n", "Bomba\n", "Shaytanat\n"],
    'Husan': ["\n Mahalla duv duv gap\n", "Jon Wick\n"]

}
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}", end='')
    for mal in kinolar:
        print(f'{mal.upper()} ', end='')



davlat = input("Davlatni kiriting: ")

davlatlar = {
    "Uzbekiston": {
        'Hududi': '448978 kv.km',
        'Aholisi': '37000000',
        'Pul birligi': "so'm"
    },
    "Rossiya": {
        'Hududi': '17098246 kv.km',
        'Aholisi': '144000000',
        'Pul birligi': 'rubl'
    },
    "AQSH": {
        'Hududi': '9631418 kv.km',
        'Aholisi': '327000000',
        'Pul birligi': 'dollar'
    },
    "Malayziya": {
        'Hududi': '329750 kv.km',
        'Aholisi': '25000000',
        'Pul birligi': 'ringgit'
    }
}

if davlat in davlatlar:
    print(f"\n{davlat.upper()}")
    for kalit, qiymat in davlatlar[davlat].items():
        print(f"{kalit}: {qiymat}")
else:
    print("Bunday davlat ro'yxatda yo'q")