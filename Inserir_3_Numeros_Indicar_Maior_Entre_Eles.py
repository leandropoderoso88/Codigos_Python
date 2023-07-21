# (f) Faça um programa que leia três números e mostre o maior deles.

numb1 = float(input("Insira o 1º numero : "))
numb2 = float(input("Insira o 2º numero : "))
numb3 = float(input("Insira o 3º numero : "))

if numb1 > numb2 and numb1 > numb3:
    print("O número " + str(numb1) + " é maior que número " + str(numb2) + " e o número " + str(numb3))
elif numb2 > numb3 and numb2 > numb1:
    print("O número " + str(numb2) + " é maior que número " + str(numb1) + " e o número " + str(numb3))
else:
    print("O número " + str(numb3) + " é maior que número " + str(numb2) + " e o número " + str(numb1))