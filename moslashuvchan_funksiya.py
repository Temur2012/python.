def summa(*sonlar):
    """Kiritilgan sonlarni yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi = yigindi + son
    return yigindi
print(summa(1,2))
print(summa(1,2,3,4,5,6))





def summa(*sonlar):
    """Kiritilgan sonlarni yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)

print(summa(4,5,6,7))






def summa(x,y,*sonlar):
    """Kiritilgan sonlarni yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)
print(summa(1,2,3,4,5,6))





def avto_info(kompaniya,model,**malumot):
    """Avto haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumot['kompaniya'] = kompaniya
    malumot['model'] = model
    return malumot
avto1=avto_info('GM','malibu',rang='qora', yili=2018,)
avto2=avto_info('Kia','K5',rang='qizil', narh=350000)
print(avto2)