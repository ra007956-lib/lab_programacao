def status_do_aluno(nota):
    if nota < 4 and nota >= 0:
        return 'Reprovado'
    elif (nota >= 4) and (nota <= 6):
        return 'Verificação Suplementar'
    elif nota > 6 and nota <= 10:
        return 'Aprovado'
    else:
        return 'Nota Inválida'
    
while True:
    nota_do_aluno = int(input('Digite a nota do aluno: '))
    print(status_do_aluno(nota_do_aluno))
    print('-'*20)
    rep = input('Deseja verificar outra nota?(S/N) ').upper()
    if rep == 'N':
        print('Verificação encerrada...')
        break