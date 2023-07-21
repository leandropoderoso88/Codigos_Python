#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
#para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
#80 euros. Informe ao utilizador da quantidades de latas de tinta a serem compradas e o
#preço total.

x = float(input("Qual o (m2) da área a ser pintada ?"))

# calcula o valor em área que deseja pintar
litro = x / 3

# Se uma lata possui um total de 18lts então calculamos o total de litros a dividis por 18 (corresponde a 1 lata)
lata = int(litro / 18)
if litro % 18 != 0:
    lata += 1

total = lata * 80
print("Para "+ str(x) + "(m2) voce irá utilizar " + str(litro) + " (lt de tinta)")
print("Você irá precisar comprar " + str(lata) + " lata.s")
print("Valor total a pagar são " + str(total) + " € correspondentes a um total " + str(lata) + " latas adquirida.s.")
#print(qttLata)