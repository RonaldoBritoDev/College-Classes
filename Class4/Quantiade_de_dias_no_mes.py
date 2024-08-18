mes = int (input('Mês: '))

if mes == 2 : 
    dias = 28
elif mes == 4  or mes == 6 or mes == 9 or mes == 11 : dias = 30 
else:
    dias = 31
print('Total de dias desse mês: ', dias)