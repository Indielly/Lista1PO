# -*- coding: utf -8 -*-
"""Faça um programa que leia e preencha uma matriz de 10x10. No final, imprima
a matriz. """

import random

matriz = [] # criando matriz maior

for i in range(10): # criando as linhas
	linha = [] 

	for j in range(10): #atribui valor para cada linha
		numero = random.randint(0,100) #gerando numeros aleatorios de 0 a 100
		linha.append(numero) # adicionando a fileira linha da matriz

	matriz.append(linha) #adicionando na matriz

#print(matriz)

for i in range(10):
	for j in range(10):
		print(f'{matriz[i][j]}\t',end='')

	print()

