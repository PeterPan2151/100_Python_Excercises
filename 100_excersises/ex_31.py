# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) 
# and the values are square of keys.

def make_dict():
    my_dict = {i:i*i for i in range(1, 21)}
    return my_dict


print(make_dict())
