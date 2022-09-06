#include <stdio.h>
#include <omp.h>

int main (void)
{

    // seta a quantidade de thread que vão ser utilizadas dentro do conjunto pragma
    omp_set_num_threads(10);


    // Printa o numero das threads utilizadas
    // No caso do meu pc, sao 8 threads (CPU de 4 nucleos)
    #pragma omp parallel
    {
        printf("Thread: %d\n", omp_get_thread_num());
    }
    printf("\nFim de uma região paralela\n\n");
    // regiões paralelas
    #pragma omp parallel
    {
        printf("Thread DE NOVO: %d\n", omp_get_thread_num());
    }
}

//gcc openMp1.c -o openmp1 -fopenmp
//./openmp1