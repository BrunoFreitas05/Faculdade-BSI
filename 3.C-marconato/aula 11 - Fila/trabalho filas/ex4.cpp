#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Definição da estrutura da pilha
typedef struct {
    char *items;
    int top;
    int size;
} Pilha;

// Função para inicializar a pilha
void inicializaPilha(Pilha *p, int size) {
    p->size = size;
    p->top = -1;
    p->items = (char *)malloc(size * sizeof(char));
}

// Função para verificar se a pilha está vazia
bool pilhaVazia(Pilha *p) {
    return p->top == -1;
}

// Função para verificar se a pilha está cheia
bool pilhaCheia(Pilha *p) {
    return p->top == p->size - 1;
}

// Função para empilhar um elemento
void empilha(Pilha *p, char x) {
    if (pilhaCheia(p)) {
        printf("Erro: a pilha está cheia\n");
        return;
    }
    p->items[++(p->top)] = x;
}

// Função para desempilhar um elemento
char desempilha(Pilha *p) {
    if (pilhaVazia(p)) {
        printf("Erro: a pilha está vazia\n");
        return '\0';
    }
    return p->items[(p->top)--];
}

// Função para liberar a memória da pilha
void liberaPilha(Pilha *p) {
    free(p->items);
}

// Função para verificar se a sequência de parênteses está bem formada
bool Verifica(Pilha *P, char *seq) {
    inicializaPilha(P, 100); // Inicializa a pilha com tamanho máximo 100
    for (int i = 0; seq[i] != '\0'; i++) {
        if (seq[i] == '(') {
            empilha(P, seq[i]);
        } else if (seq[i] == ')') {
            if (pilhaVazia(P) || desempilha(P) != '(') {
                liberaPilha(P);
                return false;
            }
        }
    }
    bool resultado = pilhaVazia(P);
    liberaPilha(P);
    return resultado;
}

int main() {
    Pilha pilha;
    char sequencia1[] = "(())()";
    char sequencia2[] = "(()))";
    char sequencia3[] = "())(";

    printf("\"%s\" -> Sequencia %s\n", sequencia1, Verifica(&pilha, sequencia1) ? "Valida!" : "Invalida!");
    printf("\"%s\" -> Sequencia %s\n", sequencia2, Verifica(&pilha, sequencia2) ? "Valida!" : "Invalida!");
    printf("\"%s\" -> Sequencia %s\n", sequencia3, Verifica(&pilha, sequencia3) ? "Valida!" : "Invalida!");

    return 0;
}

