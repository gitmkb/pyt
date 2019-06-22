# Local / Global variable
x = 'a'


def greet():
    global x
    x = 'b'

greet()
print(x)
