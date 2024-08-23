import random

sorteado = random.randint(1, 100)

acertou = False

for tent in range(1, 11) :
    print(f'Tentativa {tent}: ', end="")
    num = int(input())
    if num < sorteado : 
        print('Tente um numero maior...')
    elif num > sorteado :
        print('Tente um numero menor...')
    else:
        acertou = True
        break
if acertou :
        print(f'[Parebéns] você acerou o numero é {sorteado}')
else: 
    print(f'[Você perdeu o jogo] o número sorteado era:{sorteado}')