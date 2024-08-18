inp = int (input('inserir os 4 digitos:'))
milhar = inp//1000
resto = inp%1000
centena = resto//100
resto = resto%100
dezena = resto//10
unidade = resto%10
print('seus 4 digitos ao contrario: ', unidade*1000 + dezena*100 + centena*10 + milhar)



