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
};
