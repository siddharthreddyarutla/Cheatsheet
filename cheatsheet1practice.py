# -*- coding: utf-8 -*-
"""CheatSheet1Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g8eNtx7dSC9741ra5d2m24023WOtUngp
"""

print("Hello World")

firstname = 'Arvind'
lastname = 'Jei'
fullname = firstname + ' ' + lastname
print (fullname)

bikes = ['trek', 'redline', 'giant']

first_bike = bikes[0]

last_bike = bikes[-1]

for bike in bikes:
        print(bike)

bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')
print(bikes)



squares = []
for x in range(1, 11):
    squares.append(x**2)
print(squares)

age = 25
if age >= 18:
 print("You can vote!")

alien = {'colour': 'yellow', 'points': 5}

print("The alien's color is " + alien['colour'])

fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
 print(name + ' loves ' + str(number))

name = input("What's your name? ")
print("Hello, " + name + "!")

age = input("How old are you? ")
age = int(age)
pi = input("What's the value of pi? ")
pi = float(pi)

current_value = 1
while current_value <= 5:
   print(current_value)
   current_value += 1

def greet_user():
 print("Hello!")
greet_user()

def make_pizza(topping='bacon'):
 print("Have a " + topping + " pizza!")
make_pizza()
make_pizza('pepperoni')

class Cat():
 def __init__(self, name):
  self.name = name
def sit(self):
 print(self.name + " is sitting.")
my_cat = Cat('Peso')
print(my_cat.name + " is a great cat!")
my_cat.sit()

finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print (first_two)

