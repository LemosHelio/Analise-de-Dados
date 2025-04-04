# Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# Salário bruto.
# Quanto pagou ao IRRF.
# Quanto pagou ao INSS.
# Quanto pagou ao sindicato.
# O salário líquido.

# Entrada dos Dados
nome = input(f'Informe o nome do Funcionário: ')
vh = float(input(f'Informe o o valor recebido por hora: '))
ht = float(input(f'Informe a quantidade de Horas Trabalhadas: '))

# Processamento dos Dados
sb = ht * vh
ir = (11 / 100)
inss = (8 / 100)
sd = (5 / 100)
td = (sb * inss) + (sb * ir) + (sb * sd)
sl = sb - td

# Saida dos Dados
print(f"O Salário Bruto é R$ {sb:.2f}")
print(f"O Valor pago ao INSS foi de: {sb * inss:.2f}")
print(f"O Valor pago ao IR foi de: {sb * ir:.2f}")
print(f"O Valor pago ao Sindicato foi de: {sb * sd:.2f}")
print(f"O Salário Líquido é R$ {sl:.2f}") 