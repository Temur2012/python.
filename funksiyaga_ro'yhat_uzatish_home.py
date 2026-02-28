# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
#
# ism=input("Ismni kiriting:")
# familya=input("Familyani kiriting:")
# yosh=input("Yoshni kiriting:")
# user_data(ism,familya,yosh)


# def find_max(a, b, c):
#     maximum = max(a, b, c)
#     if a==b==c:
#         print(f"Eng katta sonlar A va B va C =  {maximum}")
#     elif a==b:
#         print(f"Eng katta sonlar A va B = {maximum}")
#     elif a==c:
#         print(f"Eng katta sonlar A va C = {maximum}")
#     elif b==c:
#         print(f"Eng katta sonlar B va C = {maximum}")
#     elif a==maximum:
#         print(f"Eng katta son A = {maximum}")
#     elif b==maximum:
#         print(f"Eng katta son B = {maximum}")
#     elif c==maximum:
#         print(f"Eng katta son C = {maximum}")
# i=int(input("A ni kiriting:"))
# m=int(input("B ni kiriting:"))
# n=int(input("C ni kiriting:"))
# find_max(i, m, n)


# def user_data(word, letter):
#     n = 0
#     for harf in word:
#         if harf == letter:
#             n = n + 1
#     print(n)

# soz = input("So'zni kiriting kiriting:")
# qidirish = input("Qidirmoqchi bo'lgan so'zni kiriting kiriting:")
# user_data(soz, qidirish)





# def list_sum(myList):
#     print("Listning elementlar yig'indisi =",sum(myList))
#
# myList = [5, 7, 10, 10]
# list_sum(myList)




# def daraja(a,b):
#     print(a**b)
# daraja(3,4)
#
#
# def daraja(a,b,c,d):
#     print(f"A ning B inchi darajasi {a**b}")
#     print(f"C ning D inchi darajasi {c**d}")
# daraja(3,4,6,7)


def digit_count_and_sum(word):
    count=0
    n=0
    for car in word:
        if car.isdigit():
            count+=1
            n+=int(car)
    print(f"Raqam soni {count}")
    print(f"yig'indi {n}")
digit_count_and_sum('ads23223')



# def add_right(a,b):
#     result = int(str(a) + str(b))
#     print(result)
# add_right(12,64)



# def add_right(a,b):
#     result = int(str(b) + str(a))
#     print(result)
# add_right(12,64)



#10







#11
def big_sales():
    sales = {
        "yanvar": 12000,
        "mart": 6000,
        "aprel": 15000,
        "sentabr": 9000,
        "dekabr": 10000,
    }

    eng_katta_oy = max(sales, key=sales.get)
    return eng_katta_oy, sales[eng_katta_oy]


print(big_sales())