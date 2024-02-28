//PROGRAMA 2 OU 1

#include <stdio.h>

main()
{	
	int a,b,c; 
	printf("digite 2 OU 1 de A:");
	scanf("%d., &a");
	printf("digite 2 OU 1 de B:");
	scanf("%d., &b");
	printf("digite 2 OU 1 de C:");
	scanf("%d., &c");
	
	if ((a==b)&&(b==c))
		printf("\nJogo empatado!");
	else
		if (b==c)
			printf("\nVenceu o A!");
	else
		if(a==c)
		printf("\nVenceu o B!");
	else
		printf("\nVenceu o C!");				
	
	
	
	
}
