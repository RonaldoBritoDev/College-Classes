nota1 = float(input('Informe o valor da nota 1: '))
nota2 = float(input('Informe o valor da nota 2: '))
nota3 = float(input('Informe o valor da nota 3: '))

if nota1<0 or nota1>10 or nota2<0 or nota2>10 or nota3<0 or nota3>10 : print('Informe uma nota de 0-10')
else:
    maior = nota1
    if nota2>maior: maior = nota2 
    if nota3>maior: maior = nota3
    media = 0.5 * maior + 0.25 * (nota1+nota2+nota3-maior)
    print('Sua media ponderada:', media)
