"""
Temario:

1.- Functions
2.- List functions
3.- Append
4.- Insert
5.- Index
6.- Max
7.- Min
8.- Count
9.- Remove
10.- Reverse
11.- String formating
12.- Format
13.- Join
14.- Replace
15.- Startswith
16.- Endswith
17.- Upper
18.- Lower
19.- Split
20.- Making your own functions
21.- Arguments
22.- Returning form functions
23.- Comments
24.- Docstrings
25.- Problema 

"""
#Functions
print("Hello world")
range(2,20)
str(3)

#List functions
#len()
nums = [1, 2, 3, 5]
print(len(nums))  #Len no empieza en 0

#append()
nums.append(6)
print(nums)

#insert()
nums.insert(1,7)   #Primer argumento es index segundo argumento es elemento
print(nums)

words = ["Python", "fun"]
index = 1
words.insert(1, "is")     #Primer argumento es index segundo argumento es elemento
print(words)

#index()
print(words.index("fun"))   #Devuelve la posición del item

#max()
nums = [1, 2, 3, 5, 2]
print(max(nums))

#min()
print(min(nums))

#count()
print(nums.count(2))

#remove()
nums.remove(2)
print(nums)

#reverse()
nums.reverse()
print(nums)

#String formatting
#format()
nums = ["hi", 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)  

a = "{x}, {y}".format(x=5, y=6)
print(a)

#join()
print(",".join(["spam","eggs","ham"]))

#replace()
print("Hello me".replace("me", "world"))

#startswith()
print("This is a sentence".startswith("This"))

#endswith()
print("This is a sentence".endswith("sentence"))

#upper()
print("This is a sentence".upper())

#lower()
print("This is a sentence".lower())

#split()
print("This is a sentence".split())
print("spam, eggs, hello".split())

#Making your own functions
def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()

#Arguments

def func(word):
    print(word + " world!")

func("Hello")

def print_sum_twice(x, y):
    print(x + y)
    print(x + y)

print_sum_twice(5,5)

#Returning from functions
def max(x, y):
    if x > y:
        return x  
    else:
        return y

max(5,10)

def num(x, y):
    total = x + y
    return total        #Todo después de return no se imprimirá
    #print("This wont be printed")

#Comments
#This is a comment

#Docstrings
"""
This is a docstring
"""

#Search engine problem
"""
Search Engine


You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
Define the search() function, so that the given code works as expected.
"""

text = input()
word = input()

def search(text,word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"

print(search(text, word))  #Respuesta
