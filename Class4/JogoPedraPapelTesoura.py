import random


jogador = input('Escolha: Pedra, Papel, Tesoura: ')
comp = random.choice(['Pedra','Papel', 'Tesoura'])
print('Computador escolheu:', comp)


if comp == jogador : 
    print('[Empate]')
elif jogador == 'Pedra' :
    if comp == 'Tesoura' : 
        print('pedra quebra tesoura, você [Ganhou]')
    else:
        print('Papel cobre pedra, você [Perdeu]')

elif jogador == 'Papel' :
    if comp == 'Pedra' : print('Pedra cobre papel, você [Ganhou]')
    else:
        print('Tesoura corta papel, você [Perdeu]')

elif comp == 'Papel' : 
    print('Tesoura corta Papel, você [Ganhou]')
else:
    print('Pedra quebra Tesoura, você [Perdeu]')