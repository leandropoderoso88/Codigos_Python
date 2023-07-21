#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando a fórmula para homens (72.7×h)−58 e para mulheres:
#(62.1 × h) − 44.7.

alt = float(input("Insira a altura da pessoa (m) : "))

mulher = (62.1 * alt)-44.7
homem = (72.7 * alt)-58

print("O peso ideal para as mulheres com " + str(alt) + "(m)" + " são " + str(mulher) + "(kg)")
print("O peso ideal para os homens com " + str(alt) + "(m)" + " são " + str(homem) + "(kg)")