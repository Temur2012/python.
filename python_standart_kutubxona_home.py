import datetime as dt

bugun = dt.date.today()
for i in range(10):
    print(bugun + dt.timedelta(days=14 * i))



ramazan=dt.date.today()
qurbonhayit=dt.date(2026,5,27)
farq=qurbonhayit-ramazan
print(f"Qurbon hayitgacha qolgan vaqt: {farq.days}")


bugun1 = dt.date.today()
birthday=dt.date(2026,12,3)
farq=bugun1-birthday
print(f"Tug'ulgan kunga: {farq.days} kun qoldi")



import re
phone = input("Telefon raqamingizni kiriting: ")
andoza = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
if re.match(andoza, phone):
    print("Raqam qabul qilindi")
else:
    print("Raqam qabul qilinmadi")





import re

matn="""🧵 Tikuvchilik biznesingiz uchun zamonaviy veb-sayt kerakmi?

LORATEX tikuvchilik firmasi uchun to‘liq funksional va zamonaviy veb-sayt ishlab chiqdik 👨‍💻

🌐 Sayt: https://loratex.uz/

🔥 Sayt imkoniyatlari:

✅ Zamonaviy va professional dizayn
✅ Mobil telefon, planshet va kompyuterga mos (Responsive)
✅ Kompaniya xizmatlari va mahsulotlari aniq ko‘rsatilgan
✅ Tez yuklanish va SEO asoslari
✅ Mijozlar ishonchini oshiruvchi tuzilma

💡 Nima uchun sayt muhim?

📌 Brendingingizni kuchaytiradi
📌 Yangi mijozlarni jalb qiladi
📌 Ishonch va professional imidj yaratadi
📌 Reklama va marketing uchun tayyor platforma

Agar siz ham:
— Tikuvchilik sexi
— Fabrika
— Atelier
— Ishlab chiqarish korxonasi
uchun shaxsiy sayt xohlasangiz — yozing 👇

📩 Buyurtma va hamkorlik uchun:
Telegram: @jonibekuralov

🚀 Biznesingizni internetga olib chiqing!"""
andoza=r'https?://[^\s]+'
sayt=re.search(andoza,matn)
print(sayt)