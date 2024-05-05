import random
n = random.randint(1, 100)
a = -1
while a != n:
    a = int(input('insira um numero de 1 a 100: '))
    if a > n:
        print('muito alto')
    elif a < n:
        print('muito baixo')
print('acertou!')