import datetime as dt

hozir=dt.datetime.now()
print(hozir)



print(hozir.date())


print(hozir.time())


print(hozir.hour)

print(hozir.minute)

print(hozir.second)

bugun=dt.date.today()
print(f"Bugungi sana: {bugun}")

ertaga=dt.date(2026,3,19)
print(f"Ertangi sana: {ertaga}")

hozir=dt.datetime.now()
vaqtHozir=hozir.time()
print(f"Hozir soat: {vaqtHozir}")

vaqrKeyin=dt.time(23,45,00)
print(f"Keyin soat: {vaqrKeyin}")

bugun=dt.date.today()
birthday=dt.date(2026,12,3)
farq=birthday-bugun
print(farq)
print(f"Tug'ulgan kunga: {farq.days} kun qoldi")


hozir=dt.datetime.now()

vaqt=hozir.strftime("%H:%M:%S")
print(f"{vaqt}")


sana=hozir.strftime("%d:%m:%Y")
print(f"Bugun sana: {sana}")

sana_vaqt=hozir.strftime("%d:%m:%Y, %H:%M")
print(sana_vaqt)













from uzwords import words
import re
andoza="^т...р$"


matches=[]
for word in words:
    if re.match(andoza,word):
        matches.append(word)
print(matches)

import re

matn="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. fmvdfbk@gmail.com, info@mail.ru
Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book"""

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email=re.findall(andoza,matn)
print(email)





andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg="Yangi parol kiriting"
msg +='(kamida 8 paroldan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg +="1 ta son va 1 ta maxsus belgilishi bo'lishi kerak): "


while True:
    passpword = input(msg)
    if re.match(andoza,passpword):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")