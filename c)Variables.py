"""
Temario:

1.- Variables
2.- Variable names
3.- Working with variables
4.- Input
5.- In-place operators
6.- Problema

"""
#Variables
user = "James"

#Variable names
"""
Puedes usar letras, números y underscores.
No puedes usar símbolos especiales o empezar la variable con un número.
Lastname y lasname no son lo mismo, python es case sensitive.

"""

#Working with variables
x = 8
print(x)

x = "This is a string" #Cambió el valor de la variable
print(x + "!")

#Input
x = input()
print(x)

name = input("Enter your name: ")
print("Hello" + name)

age = int(input("Whats your age?"))
print("His age is" + str(age))

#In-place Operators
x = 2
x += 3
print(x)

x = "eggs"
x += "spam"
print(x)

"""
Tip Calculator


When you go out to eat, you always tip 20% of the bill amount. But who’s got the time to calculate the right tip amount every time? Not you that’s for sure! You’re making a program to calculate tips and save some time.

Your program needs to take the bill amount as input and output the tip as a float.

Sample Input
50

Sample Output
10.0
Explanation: 20% of 50 is 10.
To calculate 20% of a given amount, you can multiply the number by 20 and divide it by 100: 50*20/100 = 10.0

"""
bill = int(input())
#your code goes here
print(bill * 0.20)   #Resultado