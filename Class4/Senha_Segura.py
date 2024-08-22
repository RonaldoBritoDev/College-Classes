import string
senha = (input('Informe sua senha: '))

maiuscula = False
digito = False
pontuacao = False 

if len(senha) <8:
    print('Senha muito curta!')
else:
    for letra in senha:
        if letra in string.ascii_uppercase :
            maiuscula = True
        if letra in string.digits :
            digito = True
        if letra in string.punctuation :
            pontuacao = True
    if maiuscula == False or digito == False or pontuacao == False :
            
        if maiuscula == False :
            print('Senha não contem letras maiúsculas')
        if digito == False :
            print('Senha não contem números')
        if pontuacao == False :
                print('Senha não contem caracteres')
    else:
        print('Senha forte')
                