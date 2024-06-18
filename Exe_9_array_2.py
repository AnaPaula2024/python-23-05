'''
Autor: Julio Miranda
Data: 17/06/2024
Versão: 1.0
Descrição: Estudo do tipo de dado Array(Vetor)
'''

carros = ['vVW']

carros.append('GW') #adiciona na úlima posição o valor indicado
carros.append('Ford')
carros.append('Fiat')
carros.append('Renault')
carros.append('Toyota')

print(carros)

carros.remove('Ford') #Remove item indicando o valor
print(carros)

carros.pop(3) #remove item indicando index
print(carros)

print(len(carros))#Tamanho do vetor atual
carros.pop(len(carros) - 1)#Deleta sempre a última posição do array
print(carros)

