print('PROGRAMA PARA LER ÂNGULO EM GRAU E CONVERTER PARA RADIANOS')

grau = float((input('Informe o ângulo em grau: ')))

rad = round(((grau * 3.14) / 180), 3)

print(f'O ângulo convertido em radianos fica: {rad}')