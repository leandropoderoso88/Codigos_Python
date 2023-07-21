#Faça um programa que calcule a área e o perímetro de um quadrado, pedindo o lado.

lado = float(input("Insira o valor do lado (cm): "))
#alt = int(input("Insira o valor da altura : ")


perimetro = lado*4
area = lado**2

print("O Perimetro do quadrado é : " + str(perimetro) + " cm")
print("A área do quadrado é : " + str(area) + " cm2")