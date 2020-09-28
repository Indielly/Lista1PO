# -*- coding: utf -8 -*-
"""Faça um programa que leia 10 números e calcule imprima o maior valor, o
menor valor e a média."""

minha_lista = []
for i in range(10):
	num = float(input(" Informe um número: "))
	minha_lista.append(num)

maior = max(minha_lista) # verificando o maior
menor = min(minha_lista) # verificando o menor
media = sum(minha_lista) / len(minha_lista) # calculando media 

print(" Maior: ",maior)
print(" Menor: ",menor)
print(" Média: ",media)



