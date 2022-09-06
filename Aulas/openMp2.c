#include <stdio.h>
#include <omp.h>
#include <string.h>

int main (void)
{
    omp_set_num_threads(4);

    // roda em paralelo
    printf("\nRoda em paralelo\n");
    #pragma omp parallel
    {
        printf("Thread: %d\n", omp_get_thread_num());

        // gera um for que roda de maneira paralela entra as threads definidas
        #pragma omp for
        for(int i=0; i<6; i++){
            printf("thread %d: iteração %d\n", omp_get_thread_num(), i);
        }
    }

    printf("\nFim do grupo\n\n");

    //paralelizar apenas um for
    printf("\nParalelizar apenas um for\n");

    #pragma omp parallel for
        for(int i=0; i<6; i++){
            printf("thread %d: iteração %d\n", omp_get_thread_num(), i);
        }

    printf("\nFim do grupo\n\n");


    printf("\nEle tenta dividir a carga de trabalho em partes iguais\n");
    // Por padrao, o omp tentar separar as threads com numeros iguais
    int n=100;
    int vetor[omp_get_max_threads()];
    memset(vetor, 0, 4*omp_get_max_threads());
    #pragma omp parallel for
        for(int i=0; i<n; i++){
            vetor[omp_get_thread_num()]++;
        }

        for(int i=0; i<omp_get_max_threads(); i++){
            printf("Thread %d executou %d iterações\n", i, vetor[i]);
        }

    printf("\nFim do grupo\n\n");
}


//gcc openMp2.c -o openmp2 -fopenmp
//./openmp2