# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
# calcular a média alcançada por aluno e apresentar:
#• A mensagem "Aprovado", se a média alcançada for maior ou igual a 9.5 e menor que 19;
#• A mensagem "Reprovado", se a média for menor do que 9.5;
#• A mensagem "Aprovado com Distinção", se a média for maior que 19.

nota1 = float(input("Insera a nota obtida na 1ª avaliação : "))
nota2 = float(input("Insera a nota obtida na 2ª avaliação : "))

media = float(nota1 + nota2)/2

if media >= 9.5 and media < 19:
    print("Aluno APROVADO com média : " + str(media))
elif media >= 19 :
    print("Aluno APROVADO COM DISNTINÇÃO,  média obtida: " + str(media))
else:
    print("Aluno REPROVADO : " + str(media) + " Deve estudar mais! ")