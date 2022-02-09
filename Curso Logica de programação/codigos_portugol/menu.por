programa
{
	
	funcao inicio()
	{
		escreva("Escolha uma das opções: \n1 - Abrir Netflix \n2 - Abrir Amazon Prime \n3 - Abrir HBO GO \n4 - Sair")
		inteiro menu= 0
		escreva("\n\nDigite sua escolha: ")
		leia(menu)
		
		escolha(menu)
		{
			caso 1:
			escreva("OK! Abrindo Netflix!!")
			pare

			caso 2:
			escreva("OK! Abrindo Amazon Prime!!")
			pare

			caso 3:
			escreva("OK! Abrindo HBO GO!!")
			pare

			caso 4:
			escreva("OK! Saindo do menu... ")
			pare

			caso contrario:
			escreva("Voce deve escolher entre as opções possiveis: 1, 2, 3 e 4")
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 394; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */