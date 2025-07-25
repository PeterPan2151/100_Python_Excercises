# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

text = input('Enter text: ')
letters = {'upper': 0, 'lower': 0}

for i in text:
    if i.isupper():
        letters['upper'] += 1
    elif i.islower():
        letters['lower'] += 1

print(f'Upper Case: {letters['upper']}')
print(f'Lower case: {letters['lower']}')
