# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# mehmonlar=['Jonibek', 'Temurbek', 'Javlonbek', "O'tkirbek", 'Anvar', 'Bekzod']
# print("sorted()qaytargan ro'yhat:", sorted(mehmonlar))
# print("Asl ro'yhat o'zgarmas qoldi:", mehmonlar)

# print(sorted(mehmonlar, reverse=True))

# ages=[12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits=['pear','banan','apple'.'watermelon','lemon']
# fruits.reverse()
# print(fruits)

# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# sonlar = list(range(0,10)) #
# print(sonlar)

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3-indeksgacha ajratib olamiz
# print(my_cars)

# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)

# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'

# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)






# mehmonlar = [‘Jonibek', ‘Temurbek', ‘Javlonbek’, ’O\’tkirbek’]
# for mehmon in mehmonlar:
#     print(mehmon)

# mehmonlar = [‘Jonibek', ‘Temurbek', ‘Javlonbek’, ’O\’tkirbek’]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-Mart kuni oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")

# mehmonlar = [‘Jonibek', ‘Temurbek', ‘Javlonbek’, ’O\’tkirbek’]
# for mehmon in mehmonlar:
# print(f"Hurmatli {mehmon}, sizni 20-Mart kuni oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")

# mehmonlar = [‘Jonibek', ‘Temurbek', ‘Javlonbek’, ’O\’tkirbek’]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-Mart kuni oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek’, ’O\’tkirbek’
# for mehmon in mehmonlar:
#     print(mehmon)
#
# print(mehmonlar)  # bu qator tsikl tashqarisida bo'lishi kerak edi

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek’, ’O\’tkirbek’]
# for mehmon in mehmonlar:
#     print(mehmon)
#
# print(mehmonlar)

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
#
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)
