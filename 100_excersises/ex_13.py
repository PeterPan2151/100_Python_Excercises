# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123
# Then, the output should be:

# LETTERS 10
# DIGITS 3
text = input('Enter text: ')
letters = 0
numbers = 0
for i in text:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        numbers +=1

print(f'Letters: {letters}')
print(f'Numbers: {numbers}')
