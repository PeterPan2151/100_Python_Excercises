# Write a program that accepts sequence of lines as input and prints the lines after making all 
# characters in the sentence capitalized.

# Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect
# Then, the output should be:

# HELLO WORLD
# PRACTICE MAKES PERFECT
text_lines = []
while True:
    text = input()

    if len(text) == 0:
        break
    else:
        text_lines.append(text)

for i in text_lines:
    print(i.upper())