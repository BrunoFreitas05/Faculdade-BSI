#include <stdio.h>
#include <conio.h>

main () {
	int x = 10, y = 20;
	int *ponteiro1, *ponteiro2;
	
	ponteiro1 = &x;
	ponteiro2 = &y;
	
	printf("\nO valor de ponteiro 1 (endereco de x): %p", ponteiro1); // valor de ponteiro1, endereco de x (ponteiro1)
	printf("\nO conteudo de ponteiro 1 (valor de x): %d\n", *ponteiro1); // valor de x, conteudo de ponteiro1 (*ponteiro1)

	printf("\nO valor de ponteiro 2 (endereco de y): %p", ponteiro2); // valor de ponteiro2, endereco de y (ponteiro2)
	printf("\nO conteudo de ponteiro 2 (valor de y): %d", *ponteiro2); // valor de y, conteudo de ponteiro2 (*ponteiro2)
	
	*ponteiro1= *ponteiro2; //isto e equivalente a x=y
	printf("\nO valor de x : %d", x);
	printf("\nO valor de y : %d", y);
	ponteiro2 = ponteiro1;
	
	*ponteiro2 = 30; //alterando o valor da variavel x
	// mostrando os valores de x e *ponteiro1 na tela
	printf("\nValor de x = %d e Conteudo de Ponteiro1 = %d", x, *ponteiro1);
	
	
	
};
