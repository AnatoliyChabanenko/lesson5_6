import random
a = random.randint(1, 10)
b = random.randint(1, 10)
v = random.choice(['-', '+', '*'])
print (f'какой результат {a}{v}{b}?:')
c = int(input())
if v == '+':
    g=(a + b)
    if g==c:
        print('hi')
    if g!=c:
        print ('нужно учить сложение')
if v == '-':
    b=(a - b)
    if b==c:
        print ('ho')
if v == '*':
    j= (a * b)
    if j == c:
        print ('ha')

