horario_inicio = int (input('Informe a hora inicial do jogo:'))
minuto_inicio = int (input('informe o minuto inicial do jogo:'))
hora_fim = int (input('Informe a hora fim do jogo:'))
minuto_fim = int (input('informe o minuto do fim do jogo:'))

horarioinicial = horario_inicio * 60 + minuto_inicio
horariofinal = hora_fim * 60 + minuto_fim

if horarioinicial < horariofinal : duracao = horariofinal - horarioinicial
else: duracao = 24* 60 - horarioinicial + horariofinal

print('Horas:', duracao//60 )
print('minutos:', duracao%60)

