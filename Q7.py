"""  Write a Python program to calculate the LCM (Least
 Common Multiple) of two numbers.
     number1 = 12, number2 = 18
     LCM of 12 and 18 are: 36
"""

def calculate_Lcm(x, y):
  
    if x > y:
        greater = x
    else :
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
         lcm = greater
         break
        greater += 1
    return lcm

number1 = 12
number2 = 18

print(f"LCM of {number1} and {number2} are: {calculate_Lcm(number1, number2)}")
