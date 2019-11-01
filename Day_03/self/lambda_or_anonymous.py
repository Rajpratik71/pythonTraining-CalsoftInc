# Simple lambda function to get square root

simple_lambda_fun = lambda x: x * x

num = int(input(" Enter the no : "))

print(simple_lambda_fun(num))

# Simple lambda function in combination with  filter()

# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

# Output: [4, 6, 8, 12]
print(new_list)

# Simple lambda function in combination with map()

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
