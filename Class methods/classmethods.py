'''
@Author: Matheus Barros
Date: 02/15/2021

'''

import Classes as cl

emp = cl.Employee.from_file("name.txt")

print(emp.name)