continuar = 'sim'
soma = 0
contagem = 0
nota = 0

while continuar == 'sim':   
    nota = int(input('Insira um número aqui: '))
    if nota >= 0:
        soma += nota
        contagem += 1
        media = (soma/contagem)
        print(f'a média dos números é: {media:.2f}')
        continuar = input('se deseja continuar digite sim, se não aperte Enter: ')
    else:
        print('numero negativo')