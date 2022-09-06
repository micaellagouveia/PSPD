#include <stdio.h>
#include <omp.h>
#include <string.h>
#include <stdlib.h>

int main (void)
{
    omp_set_num_threads(4);

    // Lança a qtd de threads definidas
    #pragma omp parallel
    {
        // Indepente da qtd de theads definida, ele pega quantas ele vai 
        // precisar para executar (1 por section)
        #pragma omp sections
        {
            // uma thread vai executar essa sessão
            #pragma omp section
            {
                printf("Uma sessão!\n");
            }

            // uma outra thread vai executar essa sessão
            #pragma omp section
            {
                printf("Outra sessão!\n");
            }
        }
        printf("Fora da section\n");
    }
}


//gcc openMp5.c -o openmp5 -fopenmp
//./openmp5