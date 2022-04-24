#Descobrir se o numero é primo

# a = int(input("Digite o número: "))

# cont = 0

# for x in range(1,a+1):
#     resto = a % x
#     if(resto == 0):
#         cont+=1

# if (cont == 2):
#     print('O número {} é primo !!\n'.format(a))
# else:
#     print('O número {} não é primo !!\n'.format(a))

#TODOS OS PRIMOS ATE 100
for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if(resto == 0):
            div+=1
    if(div == 2):
        print(num)