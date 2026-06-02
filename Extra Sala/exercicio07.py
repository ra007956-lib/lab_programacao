pares = []
impares = []

for i in range(1, 10+1):
    while True:
        num = int(input(f'Digite o {i}º número: '))
        if num in pares or num in impares:
            print('Esse número já está na lista.')
        else:
            break
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('==== OS NÚMEROS PARES SÃO ====')
for i in pares:
    print(i, end=', ' if not i == pares[-1] else '.\n')

print('==== OS NÚMEROS ÍMPARES SÃO ====')
for i in impares:
    print(i, end=', ' if not i == impares[-1] else '.\n')
    
