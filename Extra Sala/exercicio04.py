notas = []
for i in range(1,5 + 1):
    nota = float(input(f'Digite a nota do aluno {i}: '))
    notas.append(nota)
notas.remove(min(notas))
print('As notas restantes são:')
for i in notas:
    print(i)