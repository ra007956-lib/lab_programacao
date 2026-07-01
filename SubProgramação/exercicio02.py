def celsius_para_fahrenheit(graus_celsius):
    F = graus_celsius * 1.8 + 32
    return F

while True:
    celsius = float(input('Digite a temperatura em Celsius: '))
    print('-----CONVERSÃO DE CELSIUS PARA FAHRENHEIT-----')
    print(f'\nTEMPERATURA EM CELSIUS: {celsius}')
    print(f'\nTEMPERATURA EM FAHREINHEIT: {celsius_para_fahrenheit(celsius):.2f}')
    print('-'*36)

    rep = input('Deseja verificar outra temperatura?(S/N) ').upper()
    if rep == 'N':
        print('Verificação encerrada...')
        break
