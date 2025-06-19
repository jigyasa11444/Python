"""
Write a Python program to reverse the order of
 words in a given sentence.
  Input_sentence = “Hello, World! Welcome to Python
 programming.”
     Output after reverse = “programming. Python to Welcome
 World! Hello,
"""
inputSentance = "Hello, World! Welcome to Python programming."

words = inputSentance.split()
reversedWord = words[::-1]
reversedStr = ' '.join(reversedWord)

print(reversedStr)