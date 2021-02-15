'''
@Author: Matheus Barros
Date: 02/15/2021

'''
import Classes as cl 

account = cl.SavingsAccount(15000)
account.withdraw(5000)

print(account.balance)
