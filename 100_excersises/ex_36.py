# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print all values except the first 5 elements in the list.

def list_square():
    squared_list = [i*i for i in range(1, 21)]
    
    return squared_list[4:]

print(list_square())
