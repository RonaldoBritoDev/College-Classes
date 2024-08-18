tempo = int(input("Informe a quantiade "))
horas = tempo//3600
print('Horas:', horas)
resto = tempo%3600

minutos = resto//60
print('minutos:', minutos)

segundos = resto%60
print('segundos:', segundos)