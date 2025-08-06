# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
# The function should just print the keys only.

def make_dict():
    my_dict = {i:i*i for i in range(1, 21)}
    for i in my_dict.keys():
        print(i)


make_dict()
