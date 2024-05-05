def avalia_projeto(f1, f2, f3, f4, s1):
    media = (f1+f2+f3+f4)/4
    if media >= 9:
        print('a bolsa será concedida')
        if s1 == 'GD':
            print(3100)
        elif s1 == 'IC':
            print(700)
        else:
            print(2100)
    else:
        print('a bolsa não será concedida')

nota1 = float(input('insira sua nota: '))
nota2 = float(input('insira sua nota: '))
nota3 = float(input('insira sua nota: '))
nota4 = float(input('insira sua nota: '))

modalidade = input('coloque o nome do curso que você deseja ter a bolsa: ')

x = avalia_projeto(nota1, nota2, nota3, nota4, modalidade)