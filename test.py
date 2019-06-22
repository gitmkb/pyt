# to comment multiple lines Ctrl /
# Alt Up/ Down arrow key: to move selected line up/ down
# first = "Mukesh"
# last = "Kumar"
# fullname = first + " " + last
# print(fullname)

first = "MK"
last = "Bhanu"
fullname = f"{first} {last}"
print(fullname)
full = f"{len(first)} {len(last)}"
print(full)

# Local / Global variable
x = 'a'


def greet():
    global x    #bad practice
    x = 'b'

greet()
print(x)
