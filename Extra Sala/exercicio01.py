while True:
    num = int(input('Digite um número (0 - para sair): '))
    if num == 0:
        print('Encerrando...')
        break
    if num >= 10 and num <= 50:
        print('Dado Válido!')
    else:
        print('Dado Inválido! Tente novamente')