# conjunto = {1,2,3,4,4,2}
# conjunto.add(5) #adiciona o elemento '5' no conjunto
# conjunto.discard(2) #remove o elemento '2' do conjunto
# print(conjunto)

conjunto1= {1,2,2,3,4,5}
conjunto2= {5,6,6,7,8}

conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_inter = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_inter))

conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre A e B: {}'.format(conjunto_diferenca1))
print('Diferença entre B e A: {}'.format(conjunto_diferenca2))

conjunto_dif_simetrica =conjunto1.symmetric_difference(conjunto2)
print('Diferença simetrica: {}'.format(conjunto_dif_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro','cachorro','gato','gato','elefante']
conjunto_animais = set(lista) #Convertendo de lista para conjunto
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)