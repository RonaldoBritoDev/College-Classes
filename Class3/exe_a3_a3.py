inp = int (input('inserir os 4 digitos:'))
if inp <1111 or inp>9999 : print('valor nao contem 4 digitos')
else:
    milhar = inp//1000
    resto = inp%1000
    centena = resto//100
    resto = resto%100
    dezena = resto//10
    unidade = resto%10
    invertido = unidade*1000 + dezena*100 + centena*10 + milhar
    print('valor ao contrario:', invertido)
    if inp == invertido : print('capicua')
    else: print('não é capicua')


    7667