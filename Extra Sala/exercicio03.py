while True:
    palavra = str(input('Digite uma palavra aleatória (quit - para sair): ')).lower()
    if palavra == 'quit':
        print('Encerrando...')
        break
    contar_vogal = 0
    for i in palavra:
        if i in 'aeiou':
            contar_vogal += 1
    print(f'A palavra "{palavra}" contém {contar_vogal} vogais!\n','='*100)

