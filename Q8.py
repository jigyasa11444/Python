"""
 Write a Python program to check if a string is an
 anagram of another string.
     string1 = "listen", string2 = "silent"
     Output: True
"""
str1 = "Listen"
str2 = "Silent"

str_A = str1.lower()
str_B = str2.lower()

if (sorted(str_A) and sorted(str_B)):
    print ("True")

    