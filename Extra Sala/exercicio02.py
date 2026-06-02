while True:
    num = int(input('Digite um número (0 - para sair): '))
    produto = 1
    if num == 0:
        print('Encerrando...')
        break
    for i in range(1, num + 1, 2):
        print(i)
        produto *= i
    print(f'O produto dos ímpares até {num} são: {produto}')
