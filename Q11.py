"""
Write a Python program to calculate the sum of
 digits of a given number until the sum becomes a
 single-digit number.
     Sample Input: num = 987
     Sample Output: Sum_of_digits = 24,
     Again compute the sum of digits so that it can be reduced
 to
     on single digit.
     Final Output: 6
"""
number = 987

while number >= 10:
    sum = 0
    while number > 0:
        sum +=  number % 10
        number //= 10
    number = sum

print("Final out: ", number)      



