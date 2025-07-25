# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class MyClass():

    def getString(self):
        my_string = input('Enter String: ')
        self.my_string = my_string
    
    def printString(self):
        print(self.my_string.upper())


obj1 = MyClass()
obj1.getString()
obj1.printString()
