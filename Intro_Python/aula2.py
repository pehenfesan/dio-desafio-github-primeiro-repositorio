from sympy import resultant


a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

soma = a + b
subtracao = a - b
multi = a * b
divi = a / b
resto = a % b

resultado = 'Soma = {} \nSubtração = {} \nMutiplicação = {} \nDivisão = {} \nResto = {}'.format(soma,subtracao,multi,divi,resto)

print(resultado)