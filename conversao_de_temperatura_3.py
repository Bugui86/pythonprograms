print('PROGRAMA PARA CONVERSÃO DE TEMPERATURA KELVIN PARA CELCIUS\n')

kelvin = float(input('Digite a temperatura em Kelvin: '))

celcius = round((kelvin - 273.15), 2)

print(f'\nA temperatura digitada em Kelvin convertida em Celcius fica:{celcius}')
