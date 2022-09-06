#include <stdio.h>
#include <omp.h>
#include <string.h>
#include <stdlib.h>

int main (void)
{
    omp_set_num_threads(4);

    srand(123);

    int *v = malloc(sizeof(int)*100000000);

    for(int i=0; i<100000000; i++) {
        v[i] = rand();

    }

    int quantidade = 0;

    #pragma omp parallel for shared(v, quantidade)

    for(int j=0; j<100000000; j++){
        if(v[j] == 0){

            #pragma omp critical
            quantidade++;
        }
    }
    printf("\nCritical\n");
    printf("quantidade de 0: %d\n", quantidade);
}


//gcc openMp4.c -o openmp4 -fopenmp
//./openmp4