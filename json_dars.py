import json

x=10
x_json=json.dumps(x)
print(type(x))
print(type(x_json))
print(x_json)



ism = "jonibek"
ism_json= json.dumps(ism)


sonlar=[12,45,23,67]
sonlar_json=json.dumps(sonlar)
print(type(sonlar))
print(type(sonlar_json))
print(sonlar_json)
print(sonlar[0])









bemor= {
    "ism":"Alijon Valiyev",
    "yosh": 30,
    "oila":True,
    "farzandlar":("Ahmad","Bonu"),
    "allergiya":None,
    "dorilar": [
        {"nomi":"Analgin","miqdori": 0.5},
        {"nomi":"Panadol","miqdori":1.2}
    ]
}


bemor_json= json.dumps(bemor, indent=4)
print(bemor_json)
print(type(bemor_json))















sonlar=[12,45,23,67]
sonlar_json=json.dumps(sonlar)
bemor= {
    "ism":"Alijon Valiyev",
    "yosh": 30,
    "oila":True,
    "farzandlar":("Ahmad","Bonu"),
    "allergiya":None,
    "dorilar": [
        {"nomi":"Analgin","miqdori": 0.5},
        {"nomi":"Panadol","miqdori":1.2}
    ]
}


bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)
print(type(bemor_json))


with open("bemor.json","w") as f:
    json.dump(bemor_json,f)
sonlar=json.loads(bemor_json)
bemor=json.loads(bemor_json)
print(sonlar)
print(type(sonlar))
print(bemor)
print(type(bemor))









import json
filename='bemor.json'
with open(filename) as f:
    bemor=json.load(f)


print(bemor)
print(type(bemor))











data={
    "address_components": [
        {
            "long_name": "Tinchlik Street",
            "short_name": "Tinchlik Street",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Khorezm",
            "short_name": "Khorezm",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Khorezm Region",
            "short_name": "Khorezm Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Tinchlik Street, Khorezm, Urgench",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.55860870120288,
            "lng": 60.6218083747805
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}

print(data["address_components"][2]["types"][1])
kenglik=data["geometry"]["location"]["lat"]
uzunlik=data["geometry"]["location"]["lng"]
print(f"{kenglik}, {uzunlik}")
















yosh=input("Yoshingizni kiriting:")
try:
    yosh=int(yosh)
    print(f"Siz {2026-yosh} yilda tug'ulgansiz")
except:
    print("Butun son kiritmadingiz")

print("Dastur Tugadi!")






x,y=5,10
try:
    y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")







mevalar=['olma','anor','anjir','uzum']
try:
    print(mevalar[7])
except IndexError:
    print(f"Ro'y xatda {len(mevalar)} ta meva bor xolos")




user={
    "username": "jonibekdev",
    "status": "admin",
    "email": "jonibekuralov5152@gmail",
    "phone":"998937564455"
}
key="tel"
try:
    print(f"Foydalanuvchi {user[key]}")
except KeyError:
    print(f"Bunday kalit mavjud emas")




n=input("Butun son kiriting:")
try:
    n=int(n)
    x=20/n
except ValueError:
    print("Butun son kiriting")
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")
else:
    print(f"x={x}")



import json
files=['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba=json.load(f)
    except FileNotFoundError:
        pass
    else:
        print(talaba['ism'])



while True:
    yosh=input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh=int(yosh)
        break

print(f"Siz {2026-yosh} yilda tug'ilgansiz")