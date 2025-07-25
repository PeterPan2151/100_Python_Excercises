# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array
# . The element value in the i-th row and j-th column of the array should be i _ j.*

# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

# Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

array_i, array_j = map(int, input().split(','))
my_array = []
for i in range(array_i):
    my_array_internal = []
    for j in range(array_j):
        my_array_internal.append(i * j)
    my_array.append(my_array_internal)
    

print(my_array)
