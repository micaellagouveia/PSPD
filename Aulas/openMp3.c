#include <stdio.h>
#include <omp.h>
#include <string.h>

int main (void)
{
    omp_set_num_threads(4);
    int n=100;
    int i=0;
    int vetor[omp_get_max_threads()];

    printf("\nVariáveis Privadas (PERIGO)\n");

    memset(vetor, 0, 4*omp_get_max_threads());
    #pragma omp parallel for private(vetor, n)
        for(int i=0; i<n; i++){
            vetor[omp_get_thread_num()]++;
        }

        for(int i=0; i<omp_get_max_threads(); i++){
            printf("Thread %d executou %d iterações\n", i, vetor[i]);
        }

    printf("\nFim do grupo\n\n");
    printf("\nVariáveis Compartilhadas\n");

    memset(vetor, 0, 4*omp_get_max_threads());
    #pragma omp parallel for shared(vetor, n) private(i)
        for(i=0; i<n; i++){
            vetor[omp_get_thread_num()]++;
        }

        for(int i=0; i<omp_get_max_threads(); i++){
            printf("Thread %d executou %d iterações\n", i, vetor[i]);
        }

    printf("\nFim do grupo\n\n");
}


//gcc openMp2.c -o openmp2 -fopenmp
//./openmp2