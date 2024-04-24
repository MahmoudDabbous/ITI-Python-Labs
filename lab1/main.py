# Write a Python program which accepts the user's first and last name and print them in 
# reverse order with a space between them.

firstName = input("Enter first Name\n")
lastName = input("Enter last Name\n")
print("Hello " + lastName + " " + firstName)


# Write a Python program that accepts an integer (n) and computes the value of 
# n+nn+nnn.  
# Sample value of n is ​ 5 
# Expected Result : ​ 615

number = input("Enter your Number \n");
print(int(number) + int(number + number) + int(number + number + number));


# Write a Python program to print the following here document.  
# Sample string : 
# a string that you "don't" have to escape 
# This 
# is a ....... multi-line 
# heredoc string --------> example

print('''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
''')


# Write a Python program to get the volume of a sphere with radius 6.

pi = 3.1415926535897931
radius = 6.0
volume = 4.0/3.0 * pi * radius**3
print('The volume of the sphere is:', volume)


# Write a Python program that will accept the base and height of a triangle and compute the area.

base = int(input("Enter base of triangle : "))
height = int(input("Enter height of triangle : "))
print(f"Area = {0.5 * base * height} ")

# Write a Python program to construct the following pattern, using a nested for loop. 
# Search about method  
# end=”” 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n=6
for r in range(n):
    for c in range(r):
        print('*' , end=" ")
    print()

for r in range(n-2,0,-1):
    for c in range(r):
        print('*',end=" ")
    print()
    

# Write a Python program that accepts a word from the user and reverse it. 

word = input("Enter your word : ")
reserveWord = "";
for char in range(len(word) - 1,0 , -1):
  reserveWord +=word[char]
print(reserveWord)


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

for num in range(7):
    if(num==3 or num==6): continue
    print(num)


# Write a Python program to get the Fibonacci series between 0 to 50 
# Note : The Fibonacci Sequence is the series of numbers : 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
# Every next number is found by adding up the two numbers before it. 
# Expected Output : 1 1 2 3 5 8 13 21 34

prv = 0
next = 1
num = 0
print(prv , next, end=" ")
while(num < 50):
   num = next + prv
   if(num > 50):break
   print(num , end=" ")
   prv = next
   next = num



# Write a Python program that accepts a string and calculate the number of digits and 
# letters.

string = "geeks22222for3geeks"
alpha = 0
for char in string:
   if char.isalpha():
       alpha += 1
print("Number of Digits:", len(string) - alpha)
print("Number of Letters:", alpha)