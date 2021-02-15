class Custumer:
	"""
	THIS CLASS SET INFORMATIONS OF A CUSTUMER.
	"""
	def __init__(self , new_name = '' , new_age = 0 , new_salary = 0):

		self.name = new_name
		self.age = new_age
		self.salary = new_salary


	def identify(self):

		print('My name is ' + str(self.name))
		print('My age is ' + str(self.age) + ' years old')
		print('My salary is $' + str(self.salary))