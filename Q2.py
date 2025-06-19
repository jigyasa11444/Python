""""Write a program that accepts a string as input from
 the user and calculates the number of digits and
 letters.
     Input: Hello123 
     Output: Alphabets: 5 & Number : 3 """

str = input("Enter a string")

alpha = 0
num = 0

for i in list (str):
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        num += 1

print(f"Alphabats: {alpha} & Number : {num}")