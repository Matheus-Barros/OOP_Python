'''
@Author: Matheus Barros
Date: 02/16/2021

'''

import Classes as cl

print('===========================COMPARING OBJECTS===========================\n')

print('COMPARING IF THEY ARE EQUAL')
a1 = cl.Person('Matheus','06-06-1997')
a2 = cl.Person('Matheus','06-06-1997')

print(a1 == a2)

b1 = cl.Number(1)
b2 = cl.Number(2)

print('\nCOMPARING IF THEY ARE EQUAL')
print(b1 == b2)

print('\nCOMPARING IF THEY ARE GREATER THAN')
print(b1 > b2)

print('\nCOMPARING IF THEY ARE GREATER OR EQUAL')
print(b1 >= b2)

print('\nCOMPARING IF THEY ARE LESS THAN')
print(b1 < b2)

print('\nCOMPARING IF THEY ARE LESS OR EQUAL')
print(b1 <= b2)

print('\nCOMPARING IF THEY ARE DIFFERENT')
print(b1 != b2)
