#include <stdio.h>
#include <stdlib.h>

typedef struct NO {
    int valor;
    struct NO *proximo;
} NO;

void Rem_Impar(NO **Inicio) {
    NO *atual = *Inicio;
    NO *anterior = NULL;

    while (atual != NULL) {
        if (atual->valor % 2 != 0) {  
            if (anterior == NULL) {  
                *Inicio = atual->proximo;
            } else {
                anterior->proximo = atual->proximo;
            }
            free(atual);
            return;
        }
        anterior = atual;
        atual = atual->proximo;
    }
}

void insereNo(NO **Inicio, int valor) {
    NO *novo = (NO*)malloc(sizeof(NO));
    novo->valor = valor;
    novo->proximo = *Inicio;
    *Inicio = novo;
}

void imprimeLista(NO *Inicio) {
    NO *atual = Inicio;
    while (atual != NULL) {
        printf("%d -> ", atual->valor);
        atual = atual->proximo;
    }
    printf("NULL\n");
}

int main() {
    NO *Inicio = NULL;

   
    insereNo(&Inicio, 5);
    insereNo(&Inicio, 15);
    insereNo(&Inicio, 20);
    insereNo(&Inicio, 10);
    insereNo(&Inicio, 30);

    printf("Lista antes da remocao: ");
    imprimeLista(Inicio);

    Rem_Impar(&Inicio);

    printf("Lista apos a remocao: ");
    imprimeLista(Inicio);

  
    while (Inicio != NULL) {
        NO *temp = Inicio;
        Inicio = Inicio->proximo;
        free(temp);
    }

    return 0;
}

