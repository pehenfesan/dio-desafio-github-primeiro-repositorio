//Função do programa: fazer calculos de media aritmetica
//Autor: Pedro Henrique

programa
{
	
	funcao inicio()
	{
		real nota1, nota2, nota3, nota4, media
		cadeia nome
		
		//Atribuição das notas digitadas pelo usuario para as respectivas variaveis
				
		escreva("Digite seu nome: ")
		leia(nome)
		escreva("Digite a nota 1: ")
		leia(nota1)
		escreva("Digite a nota 2: ")
		leia(nota2)
		escreva("Digite a nota 3: ")
		leia(nota3)
		escreva("Digite a nota 4: ")
		leia(nota4)

		//Calculo da media das notas
		media = (nota1 + nota2 + nota3 + nota4)/4
		
		escreva("\nSua media foi "+media)
		//Condicional para a media maior que 7 ou menor
		se(media>= 7){
			escreva("\nParabens voce foi aprovado !!")
		}senao{
			escreva("\nInfelizmente voce reprovou !!")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 578; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */