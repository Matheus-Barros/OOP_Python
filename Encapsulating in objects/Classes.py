class Custumer:
	"""
	THIS CLASS SET INFORMATIONS OF A CUSTUMER.
	"""

	def set_name(self,new_name):
		self.name = new_name


	def set_age(self,new_age):
		self.age = new_age

	
	def set_salary(self,new_salary):
		self.salary = new_salary


	def identify(self):

		#CHECKING IF THE ATTRIBUTE 'name' EXISTS
		if hasattr(self, 'name'):		
			print('My name is ' + str(self.name))

		#CHECKING IF THE ATTRIBUTE 'age' EXISTS
		if hasattr(self, 'age'):
			print('My age is ' + str(self.age) + ' years old')

		#CHECKING IF THE ATTRIBUTE 'salary' EXISTS
		if hasattr(self, 'salary'):
			print('My salary is $' + str(self.salary))