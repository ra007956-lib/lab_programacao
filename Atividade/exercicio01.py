vetor = []
cont_igual = 0
vetor_diferentes = []
cont_vetor = 0

print('-'*100)
print('INSIRA AS POSIÇÕES DO VETOR:')
print('-'*100)
for p in range(1,10+1):
    vetor.append(int(input(f'Digite a posição {p} do vetor: ')))

print('-'*100)
print('PROCESSO DE VERIFICAÇÃO:')
print('-'*100)
for p in vetor:
    if p not in vetor_diferentes:
        vetor_diferentes.append(p)
    else:
        cont_igual += 1
        print(f'{p} é um valor repetido.')

print('-'*100)
print('RESULTADO FINAL:')
print(f'Temos um total de {cont_igual} valores iguais.')
print('-'*60)
print(f'O vetor sem repetições é:')
for p in vetor_diferentes:
    print(p)
    cont_vetor += 1
print('-'*60)
print(f'Temos {cont_vetor} posições diferentes!')
print('-'*60)

