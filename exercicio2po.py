# -*- coding: utf -8 -*-
""" Faça um programa que leia 10 números e os armazene em um vetor. Imprima
o vetor."""

meu_vetor = [] #criando vetor
for i in range(10): # definindo quantas vezes vai repetir
	numero = input(" Informe um número: ")
	meu_vetor.append(int(numero)) #preenchendo vetor

print(meu_vetor)
