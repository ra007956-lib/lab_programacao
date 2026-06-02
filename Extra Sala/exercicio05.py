lista = []

for i in range(1,7):
    num = int(input(f'Digite o {i}º número: '))
    lista.append(num)

print('='*100)
verificar = int(input('Digite um número para ser verificado: '))
duplicadas = 0
for indice, i in enumerate(lista):
    if i == verificar:
        print(f'Foi verificado duplicada no índice {indice}')
        duplicadas += 1

print('='*100)
print(f'Foi possível verificar {duplicadas} duplicadas do número "{verificar}"')
        
