#(b) Faça um programa que peça um valor e mostre se o valor é positivo ou negativo.

num1 = float(input("Insira o 1º número : "))

if num1 > 0:
    print("O valor(nº) inserido " + str(num1) + " é maior que Zero.")
else:
    print("O valor(nº) inserido " + str(num1) + " é menor que Zero.")