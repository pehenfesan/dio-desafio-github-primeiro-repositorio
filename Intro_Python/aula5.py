lista = [1,3,10,8,5,2,6]
lista_animal = ['cachorro','gato','elefante']

# lista_animal.sort()
# print(lista_animal)

# print(lista_animal[1])

# print(sum(lista))
# print(max(lista))
# print(min(lista))

# print(max(lista_animal))
# print(min(lista_animal))

# print(lista)
# lista.sort()
# print(lista)

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista')
#     lista_animal.append('lobo') #adiciona um novo elemento
    
# lista_animal.pop(1) #remove o elemento da posição 1 da lista, sem o numero espeificando remove o utimo elemento
# lista_animal.remove('cachorro')  #Remove um elemento que sabemos o valor
# print(lista_animal)

# nova_lista = lista * 3 #mutiplica 3 vezes os elementos dessa lista e atribui pra variavel declarada

# print(nova_lista)

tupla = (1,2,4,7,9)

print(tupla[2])
print(len(tupla))
print(len(lista))

nova_lista = list(tupla) #trandformar uma tupla em lista
print(type(nova_lista))
print(nova_lista)

nova_tupla = tuple(lista_animal) #transformar uma lista em tupla
print(type(nova_tupla))
print(nova_tupla)