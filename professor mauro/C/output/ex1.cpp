#include <stdio.h>

main()
{
	int a,b,c, maior;
		
	printf("digite o valor de A:");
	scanf("%d., &a");
	printf("digite o valor de B:");
	scanf("%d., &b");
	printf("digite o valor de C:");
	scanf("%d., &c");
	
	if ((a>b) && (a>c))
	    maior = a;
	else
	  if (b>c)
	      maior =b;
	    else 
	      maior =c;
	printf("\nmaior = %d\n", maior);
	
	  
	}
