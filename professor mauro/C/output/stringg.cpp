#include <stdio.h>
#include <string.h>
main()
{
	char capital[40];
	printf("Digite a capital da Franca: ");
	fflush(stdin);
	gets(capital);
	printf("\nA capital possui %d letras.", strlen(capital));
}
