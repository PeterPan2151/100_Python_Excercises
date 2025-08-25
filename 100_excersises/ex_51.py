# Write a function to compute 5/0 and use try/except to catch the exceptions.
def compute():
    try:
        return 5/0
    except ZeroDivisionError:
        return "Error, zero division error"
    
print(compute())
