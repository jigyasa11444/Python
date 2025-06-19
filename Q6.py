"""
 Write a Python program to check if a given number
 is a perfect number. 
A Perfect number is a positive integer that is equal to the
 sum of its proper divisors. For instance, 6 has divisors 1, 2,
 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
     Input: 5 
     Output: No

"""
num = 28
sum = 0

for i in range(1, num ):
    if num % i == 0 :
        sum = sum + i
               

if sum == num :
    print("yes")
else:
    print("NO")            






