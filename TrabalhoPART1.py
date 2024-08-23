# Lista dos meses do ano com a primeira letra maiúscula
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Inicializa a lista das temperaturas máximas com 12 posições, uma para cada mês
temperaturas_maximas = [0] * 12

for i in range(12):
    while True:  # Loop para garantir que a entrada é válida
        try:
            # Solicita ao usuário a temperatura máxima do mês
            temperatura_maxima = float(input(f"Digite a temperatura máxima para {meses[i]} (em °C): "))
            
            # Valida se a temperatura está dentro do intervalo permitido
            if -60 <= temperatura_maxima <= 50:
                temperaturas_maximas[i] = temperatura_maxima
                break  # Sai do loop se a entrada for válida
            else:
                print("[ERRO] Temperatura fora do intervalo válido (-60°C a 50°C).")
        except ValueError:
            print("[ERRO] Entrada inválida. Por favor, insira um número.")

# Calcula a temperatura média máxima anual
soma_temperaturas = 0
for temp in temperaturas_maximas:
    soma_temperaturas += temp
media_maxima_anual = soma_temperaturas / 12

# Calcula a quantidade de meses escaldantes (acima de 33°C)
meses_escaldantes = 0
for temp in temperaturas_maximas:
    if temp > 33:
        meses_escaldantes += 1

# Determina o mês mais escaldante (com a maior temperatura)
maior_temperatura = temperaturas_maximas[0]
mes_mais_escaldante = 0

# Determina o mês menos quente (com a menor temperatura)
menor_temperatura = temperaturas_maximas[0]
mes_menos_quente = 0

# Loop para encontrar os meses com as temperaturas extremas
for i in range(1, 12):
    if temperaturas_maximas[i] > maior_temperatura:
        maior_temperatura = temperaturas_maximas[i]
        mes_mais_escaldante = i
    if temperaturas_maximas[i] < menor_temperatura:
        menor_temperatura = temperaturas_maximas[i]
        mes_menos_quente = i

# Exibe os resultados
print(f"\nTemperatura média máxima anual: {media_maxima_anual:.2f} °C")
print(f"Quantidade de meses escaldantes (acima de 33°C): {meses_escaldantes}")
print(f"Mês mais escaldante do ano: {meses[mes_mais_escaldante]}")
print(f"Mês menos quente do ano: {meses[mes_menos_quente]}")