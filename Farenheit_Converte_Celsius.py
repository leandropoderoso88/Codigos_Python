#Faça um programa que peça a temperatura em graus Farenheit, transforme e mostre a
#temperatura em graus Celsius. C = (5 × (F − 32)/9)

Farenheit = float(input("Insira a temperatura em (ºF) :"))

celsius = float((Farenheit-32)/9)*5
#celsius = float(Farenheit-32)/1.8

print("A conversão para celsius é :" + str(celsius) + " ºC")
