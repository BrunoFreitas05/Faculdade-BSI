#include <stdio.h>
main()
{
	int a,b,c, maior;
	printf("\n Digite o primeiro numero: ");
	scanf("%d",&a); 
	printf("\n Digite o segundo numero: ");
	scanf("%d",&b);
	printf("\n Digite o terceiro numero: ");
	scanf("%d",&c); 
	if ((a>b)&&(a>c)) 
		maior = a;
	else
		if (b>c)
			maior =b;
		else
			maior = c;
	printf("Maior valor = %d",maior);
				
				




}


	
