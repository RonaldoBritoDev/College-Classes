altura = float (input('Altura (cm): '))
peso = float (input('Peso (kg): '))
imc = peso/altura**2

if imc < 18.6 : print('Abaixo do peso')
elif imc <25 : print('Peso ideal')
elif imc <30 : print('Sobrepeso')
elif imc <35 : print('Obesidade grau I')
elif imc <40 : print('Obesidade grau II')
else:
    print('Obesidade grau III')