#include <stdio.h>
main()
{
	int num,soma;
	
	for(num=1,soma=0; num<=100; num++)
		soma+=num;
	printf("\Soma = %d", soma);	
}
