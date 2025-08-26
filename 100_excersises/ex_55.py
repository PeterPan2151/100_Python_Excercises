# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
text = input()
digits = [i for i in text if i.isdigit()]
print(digits)
