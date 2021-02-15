'''
@Author: Matheus Barros
Date: 02/15/2021

'''

import Classes as cl

#Creating a new instance
check_acct = cl.CheckingAccount(1000, 25)

# Will call withdraw from CheckingAccount
check_acct.withdraw(200)

# Will call withdraw from CheckingAccount
check_acct.withdraw(200, fee=15)

print(check_acct.balance)