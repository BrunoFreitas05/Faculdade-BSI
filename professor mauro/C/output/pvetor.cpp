#include <stdio.h>
#include <conio.h>
#define MAX 10

main()
{
	int i, vetor[MAX],*pvetor=NULL;
	pvetor= vetor;
	for(i=0;i<10;i++)
		*(pvetor+i)= i+1;
	for(i=0;i<MAX;i++)
		printf("\nO conteudo de pvetor[%d] = %d", i , *(pvetor+i));	
}
