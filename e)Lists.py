"""
Temario:

1.- Lists
2.- Strings like lists
3.- List operations
4.- For loops
5.- Ranges
6.- List slices
7.- Problema

"""

#Lists
words = ["Hello", "World", "!"]
print(words[0])
print(words[1])
print(words[2])

m = [
    [1,2,3],
    [4,5,6]
]  

print(m[1][2]) #Segunda fila tercer elemento [1]= fila 2 [2]=columna 3
print(m[0][1])

#Strings like lists

str1 = "Hello world!"
print(str1[6])  #los espacios también tienen index

#Lists operations

nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 3)
print(4 not in nums)
print(not 4 in nums)
print(3 not in nums)
print(not 3 in nums)

#For loops

palabras = ["Pedro", "Iván", "Pablo"]

for palabra in palabras:
    print(palabra + "!")

t = "Este es un texto"
u = t.lower()
count = 0
for x in u:
    print(x)
    
    if (x == "e"):
        count += 1
print("Hay un total de " + str(count) + " e's")

#Ranges

numbers = list(range(10))
print(numbers)

numbers1 = list(range(3,10)) #Hará una lista del 3 al 9
print(numbers1)

numbers2 = list(range(5,20,2)) #Hará una lista del 5 al 19 de dos en dos 5 = ¿de dónde quieres iniciar?
                                                                        #20 = ¿Hasta dónde quieres llegar?
                                                                        #2 = ¡de cuántos en cuántos?
print(numbers2)

numbers3 = list(range(20,5,-2)) #También se puede trabajar con números negativos
print(numbers3)

for i in range(5):
    print("Hello")

#List slices

squares = [0, 1, 14, 9,  16, 25, 36, 49, 64, 81]
print(squares[2:6]) #Imprime del tercer al sexto dígito
print(squares[0])   #Imprime el primer dígito
print(squares[:5])  #Imprime del primero al quinto
print(squares[2:])  #Imprime del tercer al final
print(squares[::2])  #Imprime de principio a final de dos en dos
print(squares[1:-2]) #Del tercer al final menos 2
print(squares[::-2])  #En reversa de dos en dos

#Problema
""" 
Sum of Consecutive Numbers


No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.

Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
You can iterate over a range and calculate the sum of all numbers in the range.
Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.
"""
N = int(input())
#your code goes 
numbers = range(0,N+1)
Sum = sum(numbers)
print(Sum) #Resultado
