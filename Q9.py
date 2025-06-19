"""
 Write a Python program to count the frequency of
 each element in a list.
     Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
     Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}

"""

inputList = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency = {}

for i in inputList:
    if i in frequency:
        frequency[i] += 1
    else: 
        frequency[i] = 1    

print("Frequency Count: ",frequency)
