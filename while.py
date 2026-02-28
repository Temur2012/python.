son = 1
while son<=5:
    print(son, end='')
    son = son+1



print("Kiriting sonning kavadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol+="(dastur to'xtatish uchun 'exit' deb yozing ): "
qiymat = ''
while qiymat != 'exit':
    qiymat= input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)


print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)


print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2)


sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
