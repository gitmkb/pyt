# conding utf-8
import pdb

pdb.set_trace()

class ExClass:
	def exmeth(self, x, y):
		print(x, y)

obj = ExClass()

# Unbound method (call)
ExClass.exmeth(obj, 0, 1)
f = ExClass.exmeth
f(obj, 8, 9)

# Bound method (call)
obj.exmeth(10, 20)
g = obj.exmeth
g(80, 90)
