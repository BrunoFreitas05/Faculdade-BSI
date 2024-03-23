#include <stdio.h>
#include <conio.h>
#define MAX_NOME 50

struct Aluno {
    int RA;
    char nome[MAX_NOME];
    float n1;
    float n2;
};

int main() {
    struct Aluno aluno;

    printf("Digite o RA do aluno: ");
    scanf("%d", &aluno.RA);

    printf("Digite o nome do aluno: ");
    scanf("%s", aluno.nome);

    printf("Digite a primeira nota do aluno: ");
    scanf("%f", &aluno.n1);

    printf("Digite a segunda nota do aluno: ");
    scanf("%f", &aluno.n2);

    float media = (aluno.n1 + aluno.n2) / 2;
    printf("A media do aluno %s e: %.2f\n", aluno.nome, media);
    return 0;
}

