import random
b = input('введите что-то:')
a = len(b)
n = random.sample(b,a)
c = ''.join (n)
print(c)