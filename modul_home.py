import random as r
n=0
sonlar=r.randint(1,100)
# print(sonlar)
while True:
    son = int(input("Sonni kiriting:"))
    n = n + 1
    if sonlar==son:
        print("Topdingiz:",n,"urunishda")
        break
    elif sonlar>son:
        print("Son kichik")
    elif sonlar<son:
        print("Son katta")
