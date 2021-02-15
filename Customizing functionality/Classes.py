class BankAccount:
	def __init__(self, balance):
		self.balance = balance
	
	def withdraw(self, amount):
		self.balance -= amount


class CheckingAccount(BankAccount):
	
	def __init__(self, balance, limit):
		BankAccount.__init__(self, balance)
		self.limit = limit
	
	def deposit(self, amount):
		self.balance += amount
	
	def withdraw(self, amount, fee=0):
		if fee <= self.limit:
			BankAccount.withdraw(self, amount - fee)
		else:
			BankAccount.withdraw(self,
			amount - self.limit)