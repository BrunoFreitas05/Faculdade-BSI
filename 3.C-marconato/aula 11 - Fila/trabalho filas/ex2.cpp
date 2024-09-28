#include <stdio.h>
#include <stdlib.h>

typedef struct dados {
    struct dados *esq; // ponteiro para o n� anterior
    int info;          // informa��o do n�
    struct dados *dir; // ponteiro para o n� posterior
} NO;

void Trans_Inicio(NO **Inicio, NO **Fim) {
    // Verifica se a lista est� vazia ou possui apenas um n�
    if (*Inicio == NULL || *Inicio == *Fim) {
        return; // N�o h� necessidade de mover o n�
    }

    // Apontador para o primeiro n�
    NO *primeiro = *Inicio;

    // Ajusta o ponteiro de In�cio para o segundo n�
    *Inicio = primeiro->dir;
    (*Inicio)->esq = NULL; // O novo primeiro n� n�o tem n� anterior

    // Ajusta o n� para ser o novo �ltimo n�
    primeiro->dir = NULL;
    primeiro->esq = *Fim;
    (*Fim)->dir = primeiro;
    *Fim = primeiro;
}

// Fun��o para criar um novo n�
NO* criarNo(int valor) {
    NO* novoNo = (NO*)malloc(sizeof(NO));
    novoNo->info = valor;
    novoNo->esq = NULL;
    novoNo->dir = NULL;
    return novoNo;
}

// Fun��o para imprimir a lista
void imprimirLista(NO *Inicio) {
    NO *atual = Inicio;
    while (atual != NULL) {
        printf("%d ", atual->info);
        atual = atual->dir;
    }
    printf("\n");
}

int main() {
    // Cria��o da lista de exemplo
    NO *Inicio = criarNo(10);
    NO *segundo = criarNo(8);
    NO *terceiro = criarNo(12);
    NO *quarto = criarNo(5);
    NO *quinto = criarNo(20);

    Inicio->dir = segundo;
    segundo->esq = Inicio;
    segundo->dir = terceiro;
    terceiro->esq = segundo;
    terceiro->dir = quarto;
    quarto->esq = terceiro;
    quarto->dir = quinto;
    quinto->esq = quarto;

    NO *Fim = quinto;

    // Imprime a lista antes da transfer�ncia
    printf("Lista antes da transfer�ncia:\n");
    imprimirLista(Inicio);

    // Transfere o primeiro n� para o fim
    Trans_Inicio(&Inicio, &Fim);

    // Imprime a lista ap�s a transfer�ncia
    printf("Lista ap�s a transfer�ncia:\n");
    imprimirLista(Inicio);

    // Libera��o de mem�ria
    NO *atual = Inicio;
    while (atual != NULL) {
        NO *prox = atual->dir;
        free(atual);
        atual = prox;
    }

    return 0;
}

