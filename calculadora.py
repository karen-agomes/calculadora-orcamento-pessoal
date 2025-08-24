print('=' * 5, "Calculadora de Orçamento Pessoal", '=' * 5)
renda = float(input('\nDigite sua renda mensal: R$'))
print('\nAgora digite suas despesas:')
alimentacao = float(input('Alimentação: R$'))
transporte = float(input('Transporte: R$'))
moradia = float(input('Moradia: R$'))
saude = float(input('Saúde: R$'))
lazer = float(input('Lazer: R$'))
outras = float(input('Outras Despesas: R$'))
print('\n', "-" * 5, "Resultado", '-' * 5)
despesas = alimentacao + transporte + moradia + saude + lazer + outras
print('\nTotal de despesas: R${:.2f}'.format(despesas))
final = renda - despesas
print('Saldo final: R${:.2f}'.format(final))
if final > 0:
    print('Você terminou o mês no positivo 🎉')
elif final < 0:
    print('Atenção: Você terminou o mês no negativo 😢')
else:
    print('Você terminou o mês no zero!')
