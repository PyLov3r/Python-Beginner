"""
Temario:

1.- Booleans
2.- Comparison
3.- If statements
4.- Nested if statements
5.- Else statements
6.- Boolean logic
7.- While loops
8.- Break 
9.- Continue
10.- BMI Problem

"""

#Booleans
my_boolean = True
print(my_boolean)

print(2 == 3)

print("Hello" == 'Hello') #True

#Comparison
x = 7
print(x == 7)
print(x != 7)
print(x < 7)
print(x > 7)
print(x <= 7)
print(x >= 7)

#if statements
#if condition:
    #statements #has indentation

x = 5
if x < 7:
    print("Correct")

#Nested if statements
num = 12

if num == 12:
    print("next")
    if num < 5:
        print("error")

#Else statements
x = 5

if x == 8:
    print("x == 8")

else:
    print("x is not 8")


y = 5

if y == 8:
    print("x is 8")
else:
    if y == 7:
        print("x is 7")
    else:
        if y == 6:
            print("x is 6")
        else:
            if y == 5:
                print("x is 5")

z = 5

if z == 6:
    print("z is 6")
elif z == 5:
    print("z is 5")
else:
    print("I dont know")

#Boolean logic

print(1 == 1 and 2 == 2)

print(1 == 1 or 2 == 2)

print(not 1 == 1) #False

#While loops

i = 3

while i < 7:
    print("Hello")
    i += 1
print("Finished")  

i = 1

while i < 10:
    if i % 2 == 0:
        print(str(i), "is even")
    else:
        print(str(i), "is odd")
    i += 1

#Break

s = 0

while True:
    print(s)
    s += 1
    if s >= 5:
        print("Breaking")
        break
    
print("Finished")

#Continue

k = 0

while True:
    k += 1
    if k == 3:
        print("Skipping")
        continue
    print(k)
    if k >=5:
        break

"""
BMI Calculator


Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal
Weight is in kg, height is in meters.
Note, that height is a float.

"""
weight = int(input())
height = float(input())
total = weight / (height**2)

if total < 18.5:
  print("Underweight")
else:
  if total == 18.5 or total < 25:
    print("Normal")
  else:
    if total == 25 or total < 30:
      print("Overweight")
    else:
      print("Obesity")
      #Respuesta


    

        
    

