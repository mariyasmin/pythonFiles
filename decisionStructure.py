# -*- coding: utf-8 -*-
"""Estrutura-de-Decisão.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zEB3_U7isnLICRa5MBDQMw-0-Tawn1MW

**Ler um valor e escrever se é positivo, negativo ou zero.**
"""

valor= int(input("Digite um valor "))

if valor > 0:
  print("O valor é positivo")

else:
  if valor < 0:
    print("O valor é negativo")
  else:
    valor == 0
    print("O valor é igual a 0")

"""**Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10,caso contrário escrever NÃO É MAIOR QUE 10!**"""

valor = int(input("Digite um valor "))
if valor >= 10:
  print ("Seu número é maior ou igual a 10")
else:
  print ("Seu número é menor que 10")

"""**Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela.**"""

valor = int(input("Digite um valor "))
valor_dois = int(input("Digite outro valor "))
soma = valor+valor_dois
if soma >= 10:
  print ("seu valor é = ", soma)
else:
  print ("seu valor é menor que 10")

"""**Entrar com um número e informar se ele é divisível por 5.**"""

valor = int(input("Digite um valor "))
if int (valor % 5 == 0):
  print ("Seu valor é divisível por 5")
else:
  print ("Seu valor não é divisível por 5")

"""**Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.**"""

valor = int(input("Digite um valor "))
if valor > 20 < 90:
  print ("Seu numero está entre 20 e 90")
else:
  print ("Seu numero não está entre 20 e 90")

"""**Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
diga se ela poderá ou não votar este ano**
"""

nasc = int(input("Digite seu ano de nascimento "))
atual = int(input("Digite o ano atual "))
if atual-nasc >= 16:
  print ("Você já pode votar, tire ou regularize seu titulo")
else:
  print ("Você ainda não tem idade para votar")

"""**Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o ano digitado é válido.**"""

nasc = int(input("Digite seu ano de nascimento "))
atual = int(input("Digite o ano atual "))
idade = atual-nasc
if idade >= 120:
  print ("a idade não é valida")
else:
  print ("você tem", idade )

"""**Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de
idade ou acima de 65 anos**
"""

idade = int (input("Digite sua idade "))
if idade >= 18 < 64:
  print ("Você é maior de idade")
else:
  if idade >= 65:
    print ("você tem mais de 65 anos")
  else:
    print ("você é de menor")

"""**Ler as notas da 1a e 2a avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a nota for igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.**"""

avaliacao1 = int (input("Digite sua primeira nota "))
avaliacao2 = int (input("Digite sua segunda nota "))
media = (avaliacao1 + avaliacao2) /2
print ("Sua média foi ", media)
if media >= 6:
  print ("Parabens, você foi aprovado!!")
else:
  print ("Não foi dessa vez, você foi reprovado :(" )

"""**Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se
este número é par ou ímpar.**
"""

valor = int(input("Digite um valor "))
if int (valor % 2 == 0):
  print ("Seu valor é par")
else:
  print ("Seu valor é impar")

"""**Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca,Paulista, Mineiro ou Outros”**"""

estado = (input("Digite a sigla do seu estado "))
if estado ==  "Rj":
  print ("Você é carioca")
else:
  if estado == "Sp":
    print ("Você é paulista")
  else:
    if estado == "Mg":
      print ("Você é mineiro")
    else:
      print ("Você é de outro estado")

"""**Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.**"""

valor = int(input("Digite um valor "))
valor2 = int(input("Digite outro valor "))
if valor > valor2:
  print ("O primeiro valor é o maior")
else:
  print ("O segundo valor é o maior")

"""**Ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.**"""

valor = int(input("Digite um valor "))
valor2 = int(input("Digite outro valor "))
if valor > valor2:
  print ("A ordem crescente é ", valor2, valor)
else:
  print ("A ordem crescente é ", valor, valor2)

"""**Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.**"""

valor = int(input("Digite um valor "))
valor2 = int(input("Digite outro valor "))
valor3 = int(input("Digite mais um valor "))
if valor > valor2 and valor > valor3:
  print ("O primeiro valor é o maior")
else:
  if valor2 > valor and valor2 > valor3:
    print ("O segundo valor é o maior")
  else:
     print ("O terceiro valor é o maior")

"""**Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.**"""

time = (input("Digite o nome do primeiro time "))
time2 = (input("Digite o nome do segundo time "))
gol = int(input("Digite a quantidade de gols do primeiro time "))
gol2 = int(input("Digite a quantidade de gols do segundo time "))
if gol > gol2:
  print ("O vencedor é ", time)
else: 
  if gol2 > gol:
    print ("O vencedor é ", time2)
  else: 
    print ("Houve um empate")