#Verificar qual numero é maior

# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))

# if(a>b and a > c):
#     print('O maior numero é {}'.format(a))
# elif(b > a and b > c):
#     print('O maior numero é {}'.format(b))
# else:
#     print('O maior numero é {}'.format(c))
# print('Final do programa !!\n')

#Verificar se há numeros pares

# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))

# resto_a = a % 2
# resto_b = b % 2

# if(resto_a == 0 or resto_b == 0):
#     print('Foi digitado algum número par!')
# else:
#     print('Não foi digitado nenhum número par !!')

#Verificando a media das notas

a = int(input("Primeira nota: "))
while(a > 10):
    a = int(input("Nota fora do intervalo permitido. Primeira nota: "))

b = int(input("Segunda nota: "))
while(b > 10):
    b = int(input("Nota fora do intervalo permitido. Segunda nota: "))

c = int(input("Terceira nota: "))
while(c > 10):
    c = int(input("Nota fora do intervalo permitido. Terceira nota: "))

d = int(input("Quarta nota: "))
while(d > 10):
    d = int(input("Nota fora do intervalo permitido. Quarta nota: "))

media = (a + b + c + d)/4

print('Media: {}'.format(media))