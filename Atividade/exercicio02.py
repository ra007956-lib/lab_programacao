vetor = []

print('-'*100)
print('DIGITE OS VALORES:')
print('-'*100)
for i in range(1,5+1):
    vetor.append(int(input(f'Digite o valor {i}: ')))

print('-'*100)
print('PROCURE O VALOR DESEJADO')
print('-'*100)
while True:    
    valor = int(input(f'Digite o valor que deseja encontrar dentro do vetor: '))

    if valor in vetor:
        position  = vetor.index(valor)
        print(f'A primeira posição do valor "{valor}" é encontrado na posição {position}.')
        print('-'*60)
        break
    else:
        print(f'Valor não encontrado, tente novamente!')
        print('-'*60)