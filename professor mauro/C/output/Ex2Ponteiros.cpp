#include <stdio.h>
#include <conio.h>
#define MAX_NOME 50
#define NUM_ALUNOS 10

struct Aluno {
    int RA;
    char nome[MAX_NOME];
    float n1;
    float n2;
};

int main() {
    struct Aluno alunos[NUM_ALUNOS];
    float media_total = 0;

    for (int i = 0; i < NUM_ALUNOS; i++) {
        printf("Digite o RA do aluno %d: ", i+1);
        scanf("%d", &alunos[i].RA);

        printf("Digite o nome do aluno %d: ", i+1);
        scanf("%s", alunos[i].nome);

        printf("Digite a primeira nota do aluno %d: ", i+1);
        scanf("%f", &alunos[i].n1);

        printf("Digite a segunda nota do aluno %d: ", i+1);
        scanf("%f", &alunos[i].n2);

        float media_aluno = (alunos[i].n1 + alunos[i].n2) / 2;
        media_total += media_aluno;
    }

    float media_final = media_total / NUM_ALUNOS;

    printf("A media das medias dos %d alunos e: %.2f\n", NUM_ALUNOS, media_final);

    getch();

    return 0;
}


