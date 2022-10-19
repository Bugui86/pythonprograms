print('PROGRAMA PARA LER UMA TEMPERATURA EM CELCIUS E CONVERTER PARA KELVIN\n')

celcius = float(input('Digite a temperatura em Celcius: '))

kelvin = round((celcius + 273.15), 2)

print(f'\nA temperatura convertida em Kelvin fica: {kelvin}')
