# leia = input
# escreva = print

name = input("Digite o seu nome: ")

nota1 = float(input("Digite a nota 1: "))  # entrada de dados com versão
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1+nota2+nota3+nota4)/4  # calculo de média

print("\nSua média é: ", media)

if media >= 60:
    print("PARABÉNS, VOCÊ PASSOU!")

else:
    print("INFELIZMENTE A SUA NOTA NÃO ALCANÇOU O MINÍMO DESEJADO...")
