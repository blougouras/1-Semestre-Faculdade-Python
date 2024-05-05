def percentual_orcamento(f1, f2, f3):
    soma = f1+f2+f3
    percentual = (soma/orcamento_familia) * 100

    return percentual

despesa1 = float(input('valor da conta de luz: '))
despesa2 = float(input('valor do aluguel: '))
despesa3 = float(input('valor da conta do mercado: '))

orcamento_familia = float(input('insira a renda familiar mensal: '))

x = percentual_orcamento(despesa1, despesa2, despesa3)

print(f'percentual = {x:.2f}% do seu orçamento.')
