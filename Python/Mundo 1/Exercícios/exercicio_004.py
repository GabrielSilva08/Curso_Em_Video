#Exercício #004 - Dissecando uma Variável
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
#Pergunta ambígua, a solução apresentada pelo professor Gustavo é essa:

a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em maiúsculas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Está capitalizado? {}'.format(a.istitle()))