n = int (input('informe a nota: '))


if n>= 90 : print('Conceito A')
else:
    if n >= 80 and n <90 : print('Conceito B')
    else:
        if n>= 70 and n <80 : print('Conceito C')
        else:
            if n>= 60 and n <70 : print('Conceito D')
            else:
                print('Conceito F')