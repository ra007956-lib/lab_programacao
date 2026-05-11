import random
dado = [1,2,3,4,5,6]
jogadas = []
cont_6 = 0

print('-'*100)
print('JOGADAS DO DADO')
print('-'*100)
for i in range(1,50+1):
    resultado = random.choice(dado)
    jogadas.append(resultado)
    if resultado == 6:
        cont_6 += 1
        if cont_6 <= 1:
            print(f'\033[32mJOGADA {i}: {resultado} - RESULTADO ENCONTRADO {cont_6} VEZ\033[0m')
        else:
            print(f'\033[32mJOGADA {i}: {resultado} - RESULTADO ENCONTRADO {cont_6} VEZES\033[0m')
    else:
        print(f'JOGADA {i}: {resultado}')

print('-'*100)
print('RESULTADO FINAL')
print('-'*100)
print(f'Foram registrados {cont_6} ocorrências da "Face 6" de 50 jogadas diferentes do dado.')
print('-'*60)


