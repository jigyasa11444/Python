"""
 Write a Python program to find the factorial of a
 number using a for loop 
"""

num = 5
fact = 1

for i in range ( 1, num + 1):
    fact = fact * i

print("Factorial: ", fact)    