otam={'ismi':'Sardor', 'yili':'1981-yilda','manzil':'Xorazmda tuĝilgan'}
print(otam)
onam={'ismi':'Anadjon', 'yili':'1985-yilda', 'manzil':'Xorazmda tuĝilgan'}
print(onam)
ukam={'ismi':'Toxir','yili':'2015yilda','manzil':'Xorazmda tuĝilgan'}
print(ukam)


taom={'ukam':'Sevimli taomi shashlik', 'singlim':'Sevimli taomi grechka', 'apkam':'Sevimli taomi qoysh', 'opom':'Sevimli taomi salat', 'akam':'Sevimli taomi osh'}
print(taom)


atama={'float':'real son',
'min':'kichikini aniqlab beradi',
'max':'kattasini aniqlaberadi',
'reverse':'rõyhatni tersaki qiladi',
'title':'har bir sõzni bosh harifini katta qiladi', 'casefold':'hamma harfni kichik qiladi', 'capitalize':'Birinchi sõzni birinchi harifini katta qiladi',
'endswith':'oxirida tugaganini aniqlab beradi', 'upper':'hamma harfni katta qiladi', 'strip':'barcha probellarni olib tashlaydi'}
print(atama)


a=input("Atamani kiriting:")
atama={'float':'real son',
'min':'kichikini aniqlab beradi',
'max':'kattasini aniqlaberadi',
'reverse':'rõyhatni tersaki qiladi',
'title':'har bir sõzni bosh harifini katta qiladi', 'casefold':'hamma harfni kichik qiladi', 'capitalize':'Birinchi sõzni birinchi harifini katta qiladi',
'endswith':'oxirida tugaganini aniqlab beradi', 'upper':'hamma harfni katta qiladi', 'strip':'barcha probellarni olib tashlaydi'}
if a.lower() in atama:
    print(atama[a])
else:
    print("Bunday sõz mavjud emas")