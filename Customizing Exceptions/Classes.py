class WrongName(Exception):pass

class Person:

	def __init__(self,name):
		
		if isinstance(name,str):
			self.name = name
		else:
			raise WrongName('Name must be a string')