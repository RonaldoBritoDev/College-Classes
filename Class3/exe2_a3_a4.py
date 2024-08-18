v1 = int (input('informe o valor 1:'))
v2 = int (input('informe o valor 2:'))
v3 = int (input('informe o valor 3:'))
v4 = int (input('informe o valor 4:'))

if v2<v1 :
    aux = v1
    v1 = v2
    v2 = aux
if v3<v1 :
    aux = v1
    v1 = v3
    v3 = aux

if v4<v1 :
    aux = v1
    v1 = v4
    v4 = aux

if v4<v2 : 
    aux = v2
    v2 = v4
    v4 = aux

if v4<v3 :
    aux = v3
    v3 = v4
    v4 = aux

if v3< v2 :
    aux = v2
    v2 = v3
    v3 = aux



print('Ordem crescente:', v1, v2, v3, v4)
print('Ordem decrescente:', v4, v3, v2, v1)