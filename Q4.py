"""
Write a Python program to find the sum of all odd
 numbers between two given numbers. 
     Start = 1, stop = 10
     Sum of odd numbers: 25

"""
num = 5
sum = 0
for i in range(num + 1):
    if i % 2 != 0 :
        sum = sum + i


print ("sum os odd number: ",sum)
