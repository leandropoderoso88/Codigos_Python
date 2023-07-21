#Faça um programa que pergunte quanto ganha por hora e o número de horas trabalhadas
#por mês. Calcule e mostre o total do salário no referido mês.

vHora = float(input("Quanto ganha por hora trabalhada (€) :"))
hTime = float(input("Total de horas trabalhadas no mês atual (h):"))

salario = float(vHora * hTime)

print("O valor a receber no mês atual será : " + str(salario) + " €")