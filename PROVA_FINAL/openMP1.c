#include <stdio.h>
#include <omp.h>

int main(){
    int tid=0, nthreads=0;
    printf("Região Serial (thread única)\n\n");

    #pragma omp parallel
    {
        tid = omp_get_thread_num();
        nthreads = omp_get_num_threads();

        printf("Regiao paralela (thread %d de %d threads\n", tid, nthreads);
    }
        tid = omp_get_thread_num();

    #pragma omp parallel num_threads(10)
    {
        nthreads = omp_get_num_threads();

        printf("Regiao paralela 2 (thread %d de %d threads\n", tid, nthreads);
    }
    printf("FIM Região Serial (thread única)\n\n");
    return 0;
}