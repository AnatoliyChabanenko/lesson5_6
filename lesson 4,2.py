'''The birthday greeting program.

Write a program that takes your name as input,
and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”

Task'''
name = input ('Как вас зовут?:')
age = int(input ('Сколько вам лет?:'))
b = age + 1

print('Hello {0}, on your next birthday you’ll be {1} years'.format(name, b) )