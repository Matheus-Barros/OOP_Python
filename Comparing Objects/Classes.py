class Person:

	def __init__(self,name,birthday):
		#FORMAT : 06-06-1997
		self.name = name
		self.birthday = birthday
		birthday_split = birthday.split('-')
		self.month = birthday_split[0]
		self.day = birthday_split[1]
		self.year = birthday_split[2]

	def __eq__(self,other):
		print('__eq__ method called')
		return (self.name == other.name) and (self.birthday == other.birthday)

class Number:
	def __init__(self,number):
		self.number = number
	
	#COMPARING IF THEY ARE EQUAL
	def __eq__(self,other):
		print('__eq__ method called')
		return self.number == other.number

	#COMPARING IF THEY ARE DIFFERENT
	def __ne__(self,other):
		print('__ne__ method called')
		return self.number != other.number

	#COMPARING IF THEY ARE GREATER OR EQUAL
	def __ge__(self,other):
		print('__ge__ method called')
		return self.number >= other.number

	#COMPARING IF THEY ARE LESS OR EQUAL
	def __le__(self,other):
		print('__le__ method called')
		return self.number <= other.number

	#COMPARING IF THEY ARE GREATER THAN
	def __gt__(self,other):
		print('__gt__ method called')
		return self.number > other.number

	#COMPARING IF THEY ARE LESS THAN
	def __lt__(self,other):
		print('__lt__ method called')
		return self.number < other.number
