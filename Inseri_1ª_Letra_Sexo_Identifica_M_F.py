#(c) Faça um programa que verifique se uma letra digitada é "F"ou "M". Conforme a letra
# escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Insira o sexo (m/f): ")

sexof = 'feminino'
sexom = 'masculino'

if sexo == 'f' or 'F':
    print("Sexo indicado (M) " + (sexof.upper()))
    print("Sexo indicado (P) " + (sexof.lower()))
    print("Sexo indicado (1º letra) " + (sexof.capitalize()))
elif sexo == 'm' or 'M':
    print("Sexo indicado (M) " + (sexom.upper()))
    print("Sexo indicado (P) " + (sexom.lower()))
    print("Sexo indicado (1º letra) " + (sexom.capitalize()))
else:
    print("Sexo não definido / inválido. ")