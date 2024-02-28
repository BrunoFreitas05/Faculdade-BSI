//Usanndo FOR...
//Faça um programa para ler N preços de produtos. Calcule e mostre o total desta compra.
//O valor de N também deve ser lido pelo teclado.

#include <stdio.h>
main()
{
	int n;
	float total, preco;
	printf("Digite o total de produtos - ");
	scanf("%d",&n);
	
	for(total=0;n>0;n--)
	{
		printf("\nDigite o preco ");
		scanf("%f",&preco);
		total += preco;
		
	}
	printf("\nTotal da compra R$ %.2f", total);
	
	
}
