#include <stdio.h>
#include <omp.h>
#define TAM 12

int main(){
   int A[TAM], B[TAM], C[TAM];
   int i;

   for (i=0; i< TAM; i++){
    A[i] = 2*i - 1;
    B[i] = i +2;
   }

   #pragma omp parallel for num_threads(4)
    for(i=0; i<TAM; i++){
        C[i] = A[i] + B[i];
        printf("Thread[%d] calculou C[%d]\n", omp_get_thread_num(), i);
    }

   for(i=0; i<TAM; i++){
    printf("C[%d]=%d\n", i, C[i]);
   }
}