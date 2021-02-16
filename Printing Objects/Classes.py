class Person:

	def __init__(self,name,birthday):
		self.name = name
		self.birthday = birthday

	#IT'S MORE USED TO REPRESENT HOW THE OBJECT REALLY IS
	def __repr__(self):
		return "Person('{name}','{birthday}')".format(name = self.name, birthday = self.birthday)

class Number:
	def __init__(self,number):
		self.number = str(number)

	#A MORE FRIENDLY WAY TO PRINT
	def __str__(self):
		message = """
		Number: {number}
		""".format(number=self.number)
		return message.strip()