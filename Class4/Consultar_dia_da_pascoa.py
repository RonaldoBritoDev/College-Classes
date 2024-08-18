ano = int (input('Ano: '))
if ano <1900 or ano >2099:
    print('Impossivel calcular!')
else:
    a = ano % 19
    b = ano % 4
    c = ano %7
    d = (19 * a + 27) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dia = 22 + d + e
    if ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076:
        dia = dia - 7
        if dia >30: 
            print('Dia da Páscoa:', dia, ' de abril')
        else: 
            print('Dia da Páscoa:', dia, ' de março')
