nome = input('Digite um nome completo: ')

inicio = True

for letra in nome :
    if inicio:
        print(f'{letra}. ', end='')
        inicio = False
    elif letra == ' ' :
        inicio = True