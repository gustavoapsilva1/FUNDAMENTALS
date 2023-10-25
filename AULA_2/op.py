
# elif = else if

import os
sair = 1
while sair == 1:

    op = int(input(
        "\n-----------------------------------------------------------------------\n\nESCOLHA UMA OPÇÃO:\n \n 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - DIVISÃO \n 4 - MULTIPLICAÇÃO\n 5 - MÉDIA\n"))

    if op == 1:

        print("\n[ SOMA ]")
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        soma = valor1+valor2
        print("\nA SOMATÓRIA DOS VALORES É: ", soma)

    elif op == 2:

        print("\n[ SUBTRAÇÃO ]")
        valor1 = float(input("Digite o valor 1: "))
        valor2 = float(input("Digite a valor 2: "))
        sub = valor1 - valor2
        print("O VALOR DA SUBITRAÍDO É: ", sub)

    elif op == 3:

        print("\n[ DIVISÃO ]")
        valor1 = float(input("Digite o valor 1: "))
        valor2 = float(input("Digite a valor 2: "))
        div = valor1 / valor2
        print("O VALOR DA DIVISÃO É ", div)

    elif op == 4:

        print("\n[ MULTIPLICAÇÃO ]")
        valor1 = float(input("Digite o valor 1: "))
        valor2 = float(input("Digite a valor 2: "))
        mult = valor1 * valor2
        print("\nO VALOR DA MULTIPLICAÇÃO É: ", mult)

    elif op == 5:

        print("\n[ MÉDIA ]")
        valor1 = float(input("Digite a nota 1: "))
        valor2 = float(input("Digite a nota 2: "))
        valor3 = float(input("Digite a nota 3: "))
        valor4 = float(input("Digite a nota 4: "))
        media = (valor1+valor2+valor3+valor4) / 4
        print("O VALOR DE MÉDIA É: ", media)

    else:
        print("\n[ OPÇÃO INVÁLIDA! ]")

    sair = int(input("\n-----------------------------------------------------------------------\nDESEJA CONTINUAR ? \n 1 - SIM \n 2 - NÃO\n"))
    os.system('cls')
