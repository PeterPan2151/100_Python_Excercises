# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500
total = 0
while True:
    text = input()
    if text:
        operation, amount = text[0], text[2:]
        if operation == 'D':
            total += int(amount)
        elif operation == 'W':
            total -= int(amount)
    else:
        break
    
print(total)
