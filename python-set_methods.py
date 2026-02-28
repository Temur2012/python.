#Python Set add() Method
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

meva= {"nok", "shaftoli", "o'rik"}
meva.add("behi")
print(meva)

#Python Set clear() Method
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

mashina = {"kia", "nexia2", "malibu"}
mashina.clear()
print(mashina)

#Python Set copy() Method
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

yoshlar= {"23", "45", "27"}
b = yoshlar.copy()
print(b)

#Python Set difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

a = {"mandarin", "gilos", "anjir"}
b = {"amzong", "yandex", "netflix"}
n = a.difference(b)
print(n)

#Python Set difference_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

a = {"kichik", "katta", "o'rta"}
b = {"len", "right", "katta"}
a.difference_update(b)
print(a)

#Python Set intersection_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "apple", "apple"}
y = {"apple", "apple", "apple"}
x.intersection_update(y)
print(x)

#Python Set isdisjoint() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"apple", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#Python Set issubset() Method
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

#Python Set issuperset() Method
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#Python Set pop() Method
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

x = {"yashil", "kok", "qizil"}
x.pop()
print(x)

#Python Set remove() Method
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("kiwi")
print(fruits)

#Python Set symmetric_difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "yandex"}
z = x.symmetric_difference(y)
print(z)

#Python Set symmetric_difference_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "outlook"}
x.symmetric_difference_update(y)
print(x)

#Python Set union() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "example"}
z = x.union(y)
print(z)

#Python Set update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "linkedln"}
x.update(y)
print(x)