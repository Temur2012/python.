mahsulotlar=[]
while True:
    mahsulot = input("Mahsulotni kiriting:")
    if mahsulot == "exit":
        break
    mahsulotlar.append(mahsulot)
print(f"Siz kiritgan maxsulotlar {mahsulotlar}")





print("E-bo'limi, maxsulotlar va narxlari")
maxsulotlar = {}
ishora = True
while ishora:
    maxsulot = input("Maxsulotni kiriting:")
    narx = input(f"{maxsulot.title()}-narxini kiriting: ")
    maxsulotlar[maxsulot] = float(narx)

    javob = input("Yana maxsulot kiritasizmi? (yes/no)")
    if javob.lower() == "no":
        ishora = False

for maxsulot, narx in maxsulotlar.items():
    print(f"{maxsulot.title()} {narx} ming")



buyurtma=[]
while True:
    mahsulot = input("Maxsulot kiriting (chiqish uchun 'exit'):")
    if mahsulot.lower() == "exit":
        break
    buyurtma.append(mahsulot)

bozor = {
    "olma": 5000,
    "banan": 12000,
    "anor": 15000,
    "uzum": 8000,
    "nok": 9000,
    "shaftoli": 11000,
    "tarvuz": 6000,
    "qovun": 7000,
    "kartoshka": 3000,
    "piyoz": 2500,
    "sabzi": 2000,
    "guruch": 14000,
    "shakar": 13000,
    "un": 10000,
    "yog'": 18000
}

for mahsulot in buyurtma:
    if mahsulot in bozor:
        print(f"{mahsulot} narxi: {bozor[mahsulot]} so'm")
    else:
        print(f"{mahsulot} - Bizda bu mahsulot yo'q")