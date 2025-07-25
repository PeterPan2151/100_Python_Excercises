nums_list = input().split(',')
squared_odd_numbers = [str(int(x) ** 2) for x in nums_list if int(x) % 2 != 0]
print(','.join(squared_odd_numbers))