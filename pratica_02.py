# - Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00.
# Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.

# Entrada de Dados
area_pintura = float(input('Informe a área a ser pintada em m2: '))

# Processamento dos Dados
lata = 18
rendimento_litro = 3
rendimento_lata = rendimento_litro * lata
valor_lt = 130

# Saida dos Dados
print(f'A quantidade de latas utilizadas para a pintura será de: {area_pintura / rendimento_lata:.2f}')
print(f'O valor total a ser pago será de: {(area_pintura / rendimento_lata) * valor_lt:.2f} reais')
