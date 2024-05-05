N = int(input('insira um numero natural para ser calculado a tabuada: '))

print(f'tabuada do {N}')
for i in range(1,11):
    resultado = N * i
    print(f"{N} x {i} = {resultado}")