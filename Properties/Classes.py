class Employer:
	def __init__(self, name, new_salary):
		self.name = name
		if new_salary < 0:
			raise ValueError("Invalid salary")
		self._salary = new_salary
	
	@property
	def salary(self):
		return self._salary
	
	@salary.setter
	def salary(self, new_salary):
		print('@salary.setter called')
		previous_salary = self.salary
		if new_salary < 0:
			raise ValueError("Invalid salary")
		self._salary = new_salary

		message = """
		Previous Salary: {previous_salary}
		New Salary setted: {actual_salary}
		""".format(previous_salary = previous_salary , actual_salary = self.salary)
		print(message)