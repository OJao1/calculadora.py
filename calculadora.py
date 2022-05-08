# -*- coding: utf-8 -*-
"""
Calculadora
Autor: João Victor
Função: Realizar Operações Matemáticas:Soma, Subtração, Divisão, Multiplicação
"""
print("-----  CALCULADORA V2.0  -----")

sair = False 

while  sair == False:

	num1 = input("Digite um número: ")
	num1 = int(num1) # int transforma string em número inteiro
	operador = input("Digite o operador (+(soma),-(subtração),/(divisão),*(multiplicação): ")
	num2 = input("Digite outro número: ")
	num2 = int(num2)

	# + soma
	if operador == "+":
		operacao = num1 + num2
	# - subtração
	if operador == "-":
		operacao = num1 - num2 
	# / divisão
	if operador == "/":
		operacao = num1 / num2
	# * multiplicação
	if operador == "*":
		operacao = num1 * num2

	print("Resultado: ")
	print(operacao)

	teste = input("Deseja continuar (n/s): ")
	if teste == "n":
		sair = True 

