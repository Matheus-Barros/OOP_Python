class Employee:
	MIN_SALARY = 30000
	def __init__(self, name, salary=30000):
		self.name = name
		if salary >= Employee.MIN_SALARY:
			self.salary = salary
		else:
			self.salary = Employee.MIN_SALARY

	#Define methods that returns an instance of the class, but aren't using the same code as __init__().
	@classmethod
	def from_file(cls, filename):
		with open(filename,"r") as f:
			name = f.readline()
		return cls(name)
