
# range = varial em repetição
# i = inteiro


somanotas = 0
for i in range(1, 11):
    nota = float(input(f"Digite a nota {i}: "))
    somanotas = somanotas + nota

media = somanotas/10


if media >= 70:
    print(f"PARABÉNS, SUA MÉDIA É {media} E A SMA DE TODAS AS NOTAS É {somanotas}")

else:
    print(f"\nINFELIZMENTE SUA MÉDIA É {media}, SENDO ASSIM A MESMA FOI ABAIXO DO MINÍMO E A SMA DE TODAS AS NOTAS É {somanotas}")
