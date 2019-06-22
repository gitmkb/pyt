from functools import reduce

num = [5, 4, 3, 8, 9, 2, 1, 6, 11, 10]
print('Python list: ', num)

evens = list(filter(lambda x: x%2==0, num))
print('Filter: ', evens)

doubles = list(map(lambda x: x*2, evens))
print('Doubles: ', doubles)

sum = reduce(lambda x, y: x+y, doubles)
print('Sum: ', sum)
