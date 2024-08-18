saldo = float(input('Informe o saldo:'))

if saldo <500: print('Sem limite')
if saldo >=500 and saldo<1000 : print('Limite:', saldo*8/100)
if saldo >1000 : print('limite:', saldo*15/100)