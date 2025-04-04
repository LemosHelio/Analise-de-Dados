# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
# sexo (masculino e feminino)
# cor dos olhos (azuis, verdes ou castanhos)
# cor dos cabelos (louros, castanhos, pretos)
# idade
#Faça um programa que determine e escreva:
#a) a maior idade dos habitantes;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

# Entrada dos Dados
sexo = []
olhos = []
cabelo = []
idade = []

# Processamento dos Dados
for i in range(3):
    sexo.append(input('Sexo F ou M? '))
    olhos.append(input('Olhos azuis, verdes ou castanhos? '))
    cabelo.append(input('Cabelo loiro, castanhos ou pretos? '))
    idade.append(int(input('Digite a idade da pessoa: ')))

maior_idade = idade[0]
sexo_f = 0
verde_loiro = 0

for i in range(len(idade)):
    if idade[i] > maior_idade:
        maior_idade = idade[i]

    if sexo == 'F' and idade >= 18 and idade <= 35:
        sexo_f += 1

    if cabelo == 'loiro' and olhos == 'verdes':
        verde_loiro += 1

# Saida dos dados
print(f'O habitante mais velho tem {maior_idade} anos')
print(f"A quantidade de mulheres entre 18 e 35 anos são: {sexo_f}")
print(f"Quantidade de pessoas com olhos verdes e cabelos loiros são: {verde_loiro}")
