tempo = float(input('insira o tempo de investimento: '))
valor = float(input('insira seu capital inicial: '))
taxa_juros = float(input('insira o taxa anual: '))

# i = 0
# while i < tempo: 
#     valor = valor *(1 + taxa_juros/100)
#     print(f'valor final : R$ {valor:.2f}')
#     i = i+1

i = 1
while i <= tempo: 
    vf = valor *(1 + taxa_juros/100)**i
    print(f'valor final : R$ {vf:.2f}')
    i = i+1