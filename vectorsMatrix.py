# -*- coding: utf-8 -*-
"""Lista de Exercícios Vetores e Matrizes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHNSH-EPxpkgW54bPWk8OS84jMI9eBSY

**1) Inicializar um vetor de inteiros com números de 0 a 99.**
"""

vetor = []
for i in range(100):
  vetor.append(i)
print(vetor)

"""**2) Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável composta chamada NOTA e calcule e imprima a sua média.**"""

notas = []
soma = 0.0
for i in range (11):
  notas.append(float(input(f"Insira sua nota[{i}]: ")))
  soma = soma + notas[i]

media = soma/10
print("Sua média é: ", media)

"""**3) Repita o algoritmo acima, porém imprima quantos valores estão acima da média.**"""

notas = []
soma = 0.0
for i in range (10):
  notas.append(float(input(f"Insira sua nota[{i}]: ")))
  soma = soma + notas[i]

media = soma/10
print("Sua média é: ", media)
conta = 0
for i in range (10):
  if notas[i] > media:
   conta = conta+1

print(f"Existem {conta} valores acima da média")

"""**4) Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o maior valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.**"""

notas = []
soma = 0
qnt = 0
for i in range (5):
  notas.append(float(input(f"Insira sua nota["+str(i)+"]: ")))
  soma = soma + notas[i]

media = soma/5
maior = notas[0]
menor = notas[0]
for i in range (5):
  if notas[i]> maior:
    maior = notas [i]
  if notas[i]< menor:
    menor= notas[i] 
  if notas[i] < media:
    qnt = qnt + 1

print("A maior nota é: ",maior)
print("A menor nota é: ",menor)
print("A média da turma é: ",media)

"""**5) Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a 30. Se existirem, escrever as posições em que estão armazenados.**"""

vetor = []
for i in range(100):
  vetor.append(i)
print(vetor)
if i == (30):
  print ({[i]})

"""**6) Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do dispositivo de entrada.**"""

vetor = []
soma = 0.0
for i in range(101):
  vetor.append(float(input(f"Insira uma variavel: ")))
  soma = soma + vetor[i]

print(vetor)
print(soma)

"""**7)Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima na ordem contrária em que foi lida.**"""

vetor = []
for i in range(201):
  vetor.append(i)
  vetor.reverse()
print(vetor)

"""**8) Classificar um vetor numérico VET de 20 elementos em ordem crescente.**"""

vetor = []
for i in range(21):
  vetor.append(input("Insira seu numero: "))
  vetor.sort()
print(vetor)

"""**9) Faça um algoritmo qualquer que leia uma matriz A de 15 linhas por 25 colunas e imprima o seu conteúdo.**"""

import random

l = 15
c = 25
A = []

for i in range (l):
  linha = []
  for j in range (c):
    valor = random.randint(1,50)
    linha.append(valor)
  A.append(linha)

for i in range(l):
  for j in range(c):
    print(f"{A[i][j]:02.0f}", end=' ')
  print()

"""**10)Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
Construa um segundo vetor formado da seguinte maneira:
• Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
• Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
• Imprima os dois vetores.**
"""

vetor1 =[]
vetor2 = [0,0,0,0,0,0,0,0,0,0,]

for i in range (10):
  vetor1.append(float(input(f"Digite o vetor 1["+str(i)+"]: ")))

for i in range(10):
  if i%2 == 0:
    vetor2[i] = vetor1[i] * 3
  else: 
    vetor2[i] = vetor1[i] / 2
  
print(vetor1)
print(vetor2)