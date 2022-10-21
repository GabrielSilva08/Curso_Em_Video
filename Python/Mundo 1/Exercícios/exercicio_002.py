#Exercício #002 - Respondendo ao Usuário
#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input("Digite seu nome: ") #"input" é o comando utilizado em python para ler algo proveniente pelo usuário. A leitura, por padrão, retorna uma string.
print("Olá {}! Seja bem vindo!".format(nome))