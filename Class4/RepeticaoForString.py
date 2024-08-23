import random

media = 0
somarendas = 0
somaidades = 0
qtdhomensmenor30 = 0
somasfilhos = 0
rendahomemmaisvelho = 0
idademaisvelho = 0
idademulhermisvelho = 0
mulhermaiorrenda = 0
idademulhermaiorrenda = 0
qtdmais3filhos = 0

totalhub = 200

for cont in range(2000) : 
    
    #sorteio
    idade = random.randint(18, 80)
    renda = random.randint(1200, 2000)
    genero = random.choice(['M','F'])
    filhos = random.randint(0,5)
    
    #1 media de rendas
    somarendas += renda
    #2 media de idade com mais de 3 filhos
    if filhos > 3 :
        somaidades += filhos
        qtdmais3filhos += 1
    #3 qnt de homens com menos de 30 anos
    if genero == 'M' and idade <30 :
        qtdhomensmenor30 += 1
    #4 media soma de filhos
        somasfilhos += filhos
    #5 renda homem mais velho
    if genero == 'M' and idade > idademaisvelho:
        idademaisvelho = idade
        rendahomemmaisvelho = renda
    if genero == 'M' and renda > mulhermaiorrenda :
        idademulhermaiorrenda = idade
        mulhermaiorrenda = renda
        
mediarendas = somarendas/totalhub
mediamais3filhos = somaidades // qtdmais3filhos
mediafilhos = somasfilhos/totalhub
print(f'media de renda: {mediarendas}')    
print(f'media de idade com mais de 3 filhos: {qtdmais3filhos}') 
print(f'total homens com menos de 30 anos:{qtdhomensmenor30}') 
print(f'media de no. de filhos:{mediafilhos}') 
print(f'renda do homem mais velho: {rendahomemmaisvelho}')
print(f'Idade da mulher com maior renda: {idademulhermaiorrenda}') 
    #mostra os resuldados