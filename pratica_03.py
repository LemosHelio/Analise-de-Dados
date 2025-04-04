#  O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.

# Entrada dos Dados
temperatura = []

# Processamento dos Dados
for i in range(5):
    temperatura.append(float(input('Informe a temperatura registrada: ')))

maior_temperatura = temperatura[0]
menor_temperatura = temperatura[0]

for i in range(len(temperatura)):
    if temperatura[i] > maior_temperatura:
        maior_temperatura = temperatura[i]
            
    if temperatura[i] < menor_temperatura:
        menor_temperatura = temperatura[i]

# Saida dos Dados
print(f'A maior temperatura registrada foi de: {maior_temperatura}°C')
print(f'A menor temperatura registrada foi de: {menor_temperatura}°C')
print(f'A media de temperatura registrada foi de: {(maior_temperatura + menor_temperatura) / 2}°C')