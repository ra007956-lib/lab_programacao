frase = str(input('Digite uma frase: '))
vetor = []

palavra = ''

for letra in frase:
    if letra != ' ':
        palavra += letra
    else:
        vetor.append(palavra)
        palavra = ''

vetor.append(palavra)

for i in vetor:
    print(i)