class BankAccount:
	def __init__(self, balance):
		self.balance = balance
	
	def withdraw(self, amount):
		self.balance -= amount

# Empty class inherited from BankAccount
class SavingsAccount(BankAccount):
	pass