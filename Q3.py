"""
Write a Python program to input marks for five
 subjects Physics, Chemistry, Biology, Mathematics,
 and Computer. Calculate the percentage and grade
 according to the following:
 Percentage >= 90% : Grade A
 Percentage >= 80% : Grade B
 Percentage >= 70% : Grade C
 Percentage >= 60% : Grade D
 Percentage >= 40% : Grade E
 Percentage < 40% : Grade F
"""

physic = int(input("physics: "))
chemistry = int(input("Chemistry: "))
biology = int(input ("Biology: "))
mathematics = int(input ("Mathematics: "))
computer = int(input ("Computer: "))

totalMarks = physic + chemistry + biology + mathematics + computer 
percentage = (totalMarks / 500 ) * 100

if percentage >= 90 :
    print("Grade A")
elif percentage >= 80 :
    print("Grade B")
elif percentage >= 70 :
    print("Grade C")
elif percentage >= 60 :
    print("Grade D")
elif percentage >= 40 :
    print("Grade E")
elif percentage < 40 :
    print("Grade F")
    
                        