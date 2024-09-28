#include <stdio.h>
#include <stdlib.h>

typedef struct dados {
    struct dados *esq; // ponteiro para o nó anterior
    int info;          // informação do nó
    struct dados *dir; // ponteiro para o nó posterior
} NO;

void Trans_Inicio(NO **Inicio, NO **Fim) {
    // Verifica se a lista está vazia ou possui apenas um nó
    if (*Inicio == NULL || *Inicio == *Fim) {
        return; // Não há necessidade de mover o nó
    }

    // Apontador para o primeiro nó
    NO *primeiro = *Inicio;

    // Ajusta o ponteiro de Início para o segundo nó
    *Inicio = primeiro->dir;
    (*Inicio)->esq = NULL; // O novo primeiro nó não tem nó anterior

    // Ajusta o nó para ser o novo último nó
    primeiro->dir = NULL;
    primeiro->esq = *Fim;
    (*Fim)->dir = primeiro;
    *Fim = primeiro;
}

// Função para criar um novo nó
NO* criarNo(int valor) {
    NO* novoNo = (NO*)malloc(sizeof(NO));
    novoNo->info = valor;
    novoNo->esq = NULL;
    novoNo->dir = NULL;
    return novoNo;
}

// Função para imprimir a lista
void imprimirLista(NO *Inicio) {
    NO *atual = Inicio;
    while (atual != NULL) {
        printf("%d ", atual->info);
        atual = atual->dir;
    }
    printf("\n");
}

int main() {
    // Criação da lista de exemplo
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

    // Imprime a lista antes da transferência
    printf("Lista antes da transferência:\n");
    imprimirLista(Inicio);

    // Transfere o primeiro nó para o fim
    Trans_Inicio(&Inicio, &Fim);

    // Imprime a lista após a transferência
    printf("Lista após a transferência:\n");
    imprimirLista(Inicio);

    // Liberação de memória
    NO *atual = Inicio;
    while (atual != NULL) {
        NO *prox = atual->dir;
        free(atual);
        atual = prox;
    }

    return 0;
}

