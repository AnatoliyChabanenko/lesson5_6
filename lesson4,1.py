'''The Guessing Game.

Write a program that generates a random number
 between 1 and 10 and lets the user guess what number was generated.
The result should be sent back
to the user via a print statement.'''
if __name__ == '__main__':
    import random
a = int(random.randint(1,10))
b = int(input ('введите число от 1 до 10:'))
if a == b :
    print (' вы угадали')
if a < b:
    print('немного больше')