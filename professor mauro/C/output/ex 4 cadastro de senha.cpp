//Supondo que a senha de cadastro seja 1234, fa�a um programa que leia uma senha e verifique se ela est� correta.
//Se estiver imprima "Acesso permitido!"  Caso esteja errado imprima: "Senha invalidal" permita que o usu�rio erre no m�ximo 3 vezes.

#include <stdio.h>
main()
{
	int senha, cont=1;
	while(cont<=3)
	{
	
		printf("Digite a senha ");
		scanf("%d",&senha);
		
		
		if (senha==1234)
		{
		
			printf("\nAcesso Permitido");
			break;
		}
		else
		{
			printf("Senha Invalida! tente Outra Vez!");
			cont++;	
		}
	}
	
	
	
	
}
