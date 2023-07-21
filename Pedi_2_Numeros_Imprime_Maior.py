#(a) Faça um programa que peça dois números e imprima o maior deles.

num1 = float(input("Insira o 1º número : "))
num2 = float(input("Insira o 2º número : "))

if num1 > num2:
    print("O 1º número inserido " + str(num1) + " é maior que o 2º número.")
else:
    print("O 2º número inserido " + str(num2) + " é maior que o 1º número.")