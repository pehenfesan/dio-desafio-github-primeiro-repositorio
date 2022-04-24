from aula7_calculadora1 import Calculadora
from aula07_televisao import Televisao

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

calculadora = Calculadora(10,5)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())