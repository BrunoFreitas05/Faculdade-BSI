#include <stdio.h>
#include <stdlib.h>

typedef struct Pilha {
    int topo;
    int capacidade;
    char* array;
} Pilha;

// Função para criar uma pilha de determinada capacidade
Pilha* cria_pilha(int capacidade) {
    Pilha* pilha = (Pilha*) malloc(sizeof(Pilha));
    pilha->capacidade = capacidade;
    pilha->topo = -1;
    pilha->array = (char*) malloc(pilha->capacidade * sizeof(char));
    return pilha;
}

// Função para verificar se a pilha está cheia
int pilha_cheia(Pilha* pilha) {
    return pilha->capacidade - 1 == pilha->topo;
}

// Função para verificar se a pilha está vazia
int pilha_vazia(Pilha* pilha) {
    return pilha->topo == -1;
}

// Função para adicionar um item à pilha
void empilhar(Pilha* pilha, char item) {
    if (!pilha_cheia(pilha)) {
        pilha->array[++pilha->topo] = item;
    }
}

// Função para remover um item da pilha
char desempilhar(Pilha* pilha) {
    if (!pilha_vazia(pilha)) {
        return pilha->array[pilha->topo--];
    }
    return '\0'; // Retorna '\0' se a pilha estiver vazia
}

void verifica(Pilha* pilha, char* sequencia) {
    for (int i = 0; sequencia[i] != '\0'; i++) {
        if (sequencia[i] == '(') {
            empilhar(pilha, sequencia[i]);
        } else if (sequencia[i] == ')') {
            if (pilha_vazia(pilha)) {
                printf("Sequencia Invalida!\n");
                return;
            }
            desempilhar(pilha);
        }
    }

    if (pilha_vazia(pilha)) {
        printf("Sequencia Valida!\n");
    } else {
        printf("Sequencia Invalida!\n");
    }
}

int main() {
    char seq1[] = "( ( ) ( ) )";
    char seq2[] = "( ( ( ) )";
    char seq3[] = ") (";

    Pilha* pilha1 = cria_pilha(100);
    Pilha* pilha2 = cria_pilha(100);
    Pilha* pilha3 = cria_pilha(100);

    verifica(pilha1, seq1);
    verifica(pilha2, seq2);
    verifica(pilha3, seq3);

    free(pilha1->array);
    free(pilha1);
    free(pilha2->array);
    free(pilha2);
    free(pilha3->array);
    free(pilha3);

    return 0;
}

