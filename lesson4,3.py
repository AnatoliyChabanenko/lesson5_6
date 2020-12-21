import random
b = input('введите что-то:')
a = len(b)
n = random.shuffle(b,a)
c = ''.join (n)
print(c)