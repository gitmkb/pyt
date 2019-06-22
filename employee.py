class Employee:
	num_of_emp = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.fname = first
		self.lname = last
		self.salary = pay
		self.email = first + '.' + last + '@company.com'
		Employee.num_of_emp += 1
	def fullname(self):
		return('{} {}'.format(self.fname, self.lname))

	def apply_raise(self):
		self.salary = int(self.salary * self.raise_amount)

print('No of employees: ', Employee.num_of_emp)
emp1 = Employee('Corey', 'Schafer', 11000)
emp2 = Employee('Mukesh', 'Kumar', 10000)
print(emp1.email + '\n' + emp2.email)
print(emp1.fullname())		#method call using Object
print(Employee.fullname(emp2))	#method call using Class
print('No of employees: ', Employee.num_of_emp)

print('\nCLASS STATIC ATTRIBUTES:')
print('Current Salary: ', emp2.salary)
print('Employee/emp2.raiseamount: ', emp2.raise_amount)
emp2.apply_raise()
print('Salary after raise: ', emp2.salary)

print('\nOBJECT\'s DICTIONARY OBJECT:')
emp1.raise_amount = 1.05	#Change for emp1 only
emp1.apply_raise()
print(emp1.__dict__)		#see that new attribute is added to emp1 object
print(emp2.__dict__)		#but emp2 still has to fallback to class for static var

print('\nCLASS DICTIONARY OBJECT:')
print(Employee.__dict__)
