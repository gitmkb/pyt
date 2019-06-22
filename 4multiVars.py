# Variable no of arguments
def multiply(*list):
	total = 1
	for i in list:
		total *= i
	return total

print('start')
print(multiply(2, 3, 4, 5, 6))
print('finish')