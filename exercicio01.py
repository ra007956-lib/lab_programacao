import random

jogadas = []
repeticoes = []

while len(jogadas) < 100:
    jogar_dado = random.randint(1,6)
    jogadas.append(jogar_dado)


repeticoes.append(jogadas.count(1))
repeticoes.append(jogadas.count(2))
repeticoes.append(jogadas.count(3))
repeticoes.append(jogadas.count(4))
repeticoes.append(jogadas.count(5))
repeticoes.append(jogadas.count(6))

print('JOGADAS DO DADO')
print(jogadas)
print('-'*100)
print(f'REPETIÇÕES\n JOGADAS COM NÚMERO 1: {repeticoes[0]}\n JOGADAS COM NÚMERO 2: {repeticoes[1]}\n JOGADAS COM NÚMERO 3: {repeticoes[2]}\n JOGADAS COM NÚMERO 4: {repeticoes[3]}\n JOGADAS COM NÚMERO 5: {repeticoes[4]}\n JOGADAS COM NÚMERO 6: {repeticoes[5]}')