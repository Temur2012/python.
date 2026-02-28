# append()  Adds an element at the end of the list
a=["olma","mandarin"]
a.append("nok")
print(a)

b=["lola"]
b.append("boychechak")
print(b)

# clear()  Removes all the elements from the list
a=["olma", "nok", "kivi"]
print(a.clear())

b=["ehbrithbbjnrthb"]
print(b.clear())

# copy()  Returns a copy of the list
fruits=["olma", "nok", "kivi"]
print(fruits.copy())

fruits=["o'rik", "ananas", "banan"]
print(fruits.copy())

#Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

mashina=["nexia", "damas"]
print(mashina.count("spark"))

#Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)

#Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

text=[2,5,8,4]
print(text.index(2))

#Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

cars=["malibu", "onix", "tracker"]
cars.insert(2,"captiva")
print(cars)

#Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

a=["board", "fyl", "direct"]
print(a.pop(1))

#Removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

text=["run", "humans", "from"]
print(text.remove("from"))

#Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
text=["try", "yellow", "loop"]
print(text.reverse())


#Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

text=["loop", "house", "board"]
print(text.sort())
