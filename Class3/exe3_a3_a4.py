preco = int (input('Informe o preço do produto:'))
if preco <0 : print('Informe um valor valido!')
if preco ==0 : print('Informe um valor superior á 0')
else:
   if preco <=10 : venda = preco + preco * 70/100 
   if preco >=10 and preco<30 : venda = preco + preco * 50/100
   if preco >=30 and preco<50 : venda = preco + preco * 40/100
   if preco >=50: venda = preco + preco * 30/100


   print('preço de venda', venda)