# -*- coding: utf-8 -*-
"""
Calculadora
Autor: João Victor
Função: Realizar Operações Matemáticas:Soma, Subtração, Divisão, Multiplicação
"""
print("-----  CALCULADORA V3.0  -----")

sair = False 

while  sair == False:

	num1 = int(input("Digite um número: "))  # int transforma string em número inteiro
	operador = input("Digite o operador (+(soma),-(subtração),/(divisão),*(multiplicação),**(elevado), */(Raiz Quadrada), /*(Raiz Cúbica): ")
	
	# */ Raiz Quadrada
	if operador == "*/":
		print(num1 ** 0.5)
	# */ Raiz Cúbica
	if operador == "/*":
		print(num1 ** 1/3)
	# + soma
	if operador == "+":
		num2 = int(input("Digite outro número: "))
		print(num1 + num2)
	# - subtração
	if operador == "-":
		num2 = int(input("Digite outro número: "))
		print(num1 - num2)  
	# / divisão
	if operador == "/":
		num2 = int(input("Digite outro número: "))
		print(num1 / num2)
	# * multiplicação
	if operador == "*":
		num2 = int(input("Digite outro número: "))
		print(num1 * num2)
	# ** Elevado
	if operador == "**":
		num2 = int(input("Digite outro número: "))
		print(num1 ** num2)

	teste = input("Deseja continuar (n/s): ")
	if teste == "n":
		sair = True 



