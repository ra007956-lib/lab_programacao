lista1 = [1,2,3,4]
lista2 = [10,20,30,40,50,60]

listaNova = []
listaMaior = len(lista2)

if len(lista1) > listaMaior:
    listaMaior = len(lista1)

interacao = 0

while interacao < listaMaior:
    if len(lista1) > interacao:
        listaNova.append(lista1[interacao])
    if len(lista2) > interacao:
        listaNova.append(lista2[interacao])
    
    interacao += 1

print(listaNova)