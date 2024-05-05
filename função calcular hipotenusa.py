import math

def calcular_hipotenusa(n1, n2):
    return math.sqrt(n1**2 + n2**2)

n1 = int(input('insira um valor para o cateto: '))
n2 = int(input('insira um valor para o cateto2: '))

hipotenusa = calcular_hipotenusa(n1,n2)

print(f'Hipotenusa = {hipotenusa:.2f}')
         
         
    
    
