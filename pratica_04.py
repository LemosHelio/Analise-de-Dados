# - Crie um programa que:
#1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
#2- Exiba a lista completa.
#3- Exiba o maior e o menor número da lista.
#4- Exiba a soma e a média de todos os números.

# Entrada dos Dados
lista = []

for i in range(10):
    lista.append(int(input("Digite um numero inteiro: ")))

maior_lista = lista[0]
menor_lista = lista[0]

for i in range(len(lista)):
    if lista[i] > maior_lista:
        maior_lista = lista[i]
            
    if lista[i] < menor_lista:
        menor_lista = lista[i]

soma = sum(lista)
media = sum(lista) / len(lista)

# Saida dos Dados
print('\nos numeros informados foram: ')
print(lista)
print(f'O maior numero informado foi: {maior_lista}')
print(f'O menor numero informado foi: {menor_lista}')
print(f'A soma dos numeros informados são: {soma}')
print(f'A media dos numeros informados são: {media:.1f}')