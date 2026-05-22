vetor = [2.5,7.5,10,4]
soma_vetor = 0

for i in vetor:
    soma_vetor += i

media = soma_vetor / len(vetor)
print('-'*100, f'\nA média é {media}\n')
possibilidade = 0
parar = 1
while parar == 1:
    for i in vetor:
        if (i <= media and i + possibilidade >= media) or (i >= media and i - possibilidade <= media):
            print(f'O número mais próximo da média é {i}.\n', '-'*100)
            parar += 1   
            break
    possibilidade += 1

