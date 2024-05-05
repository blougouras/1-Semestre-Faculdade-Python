A = float(input())
B = float(input())

media = (A + B)/2

if media >= 6:
    print('aprovado')
if media < 6 and A > 2:
    print('talvez com a sub')
else:
    print('reprovado')