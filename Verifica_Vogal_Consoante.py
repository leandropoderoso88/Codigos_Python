# (d) Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Insira uma letra : ")

vogal = ['a', 'e', 'i', 'o', 'u']
consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'w', 't', 'y', 'x', 'z']

if letra in vogal:
    print("A letra escrita " f'{letra}  pertence ao conjunto de vogais :  {vogal}')
else:
    print("A letra escrita " f'{letra}  pertence ao conjunto de consoantes : {consoante}')