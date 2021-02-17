'''
@Author: Matheus Barros
Date: 02/17/2021

'''

import Classes as cl

emp = cl.Employer('Matheus',5500)

emp.salary = 6500

#IT'LL RAISE AN ERROR, BECAUSE THE SALARY IS NEGATIVE
emp.salary = -7200
