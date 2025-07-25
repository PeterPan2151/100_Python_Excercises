# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:

# 9
# Then, the output should be:

# 11106
digit = int(input('Enter a number: '))
str_digit = ''
sum = 0
for i in range(4):
    str_digit += str(digit)
    sum += int(str_digit)

print(sum)
