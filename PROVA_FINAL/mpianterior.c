#include <stdio.h>
#include <mpi.h>
#include <sys/types.h>
#include <unistd.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#define MAX 1000
#define PACKET_SIZE 250

int main(int argc, char **argv)
{

    MPI_Init(&argc, &argv);

    int meurank, size, sum=0, i, j, k;
    int **a, **b, **c;
	MPI_Status status;
    int tam=10;
    float result[2] = {MAX, 0};

    MPI_Comm_rank(MPI_COMM_WORLD, &meurank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    	// criando um array de ponteiros
	a =(int **)malloc(tam * sizeof(int*));
	b =(int **)malloc(tam * sizeof(int*));
	c=(int **)malloc(tam * sizeof(int*));

	// alocando memória para as matrizes
	for(i = 0; i < tam; i++)
	{
		a[i]=(int *)malloc(tam * sizeof(int));
		c[i]=(int *)malloc(tam * sizeof(int));
		b[i]=(int *)malloc(tam * sizeof(int));
	}
	
	// inicializando as matrizes com valor 1
	for(i = 0; i < tam; i++)
	{
		for(j = 0; j < tam; j++)
		{
			a[i][j] = 1;
			b[i][j] = 1;
		}
	}

    // rank 0 = MASTER
    if (meurank == 0)
    {
        float V[MAX];

        // Iniciando o vetor
        for (int i = 0; i < MAX; i++)
        {
            V[i] = sqrt(pow((i - MAX / 2), 2));
            printf("V[%d]: %f\n", i, V[i]);
        }

        int flag = 0;
        float s[PACKET_SIZE];

        memset(s, 0, PACKET_SIZE);

        // Enviando partes iguais do vetor para cada SLAVE
        for (int j = 0; j < MAX + 1; j++)
        {
            if (j % PACKET_SIZE == 0 && j > 0)
            {
                flag = flag + 1;
                MPI_Send(s, PACKET_SIZE, MPI_FLOAT, flag, 0, MPI_COMM_WORLD);
                // printf("[MASTER] Enviei %f para o rank %d\n", s[0], flag);
                memset(s, 0, PACKET_SIZE);
            }
            s[j - (flag * PACKET_SIZE)] = V[j];

        }
    }

    // Ranks !=0 : São os SLAVES
    else
    {
        float receive_array[PACKET_SIZE];


        // Recebendo partes iguais do MASTER
        MPI_Recv(receive_array, PACKET_SIZE, MPI_FLOAT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        //printf("[SLAVE] (%d) recebeu %f\n", meurank, receive_array[0]);

        // Encontrando maior e menor do pacote
        for (int i = 0; i < PACKET_SIZE; i++)
        {
            receive_array[i] = receive_array[i];
            if (receive_array[i] < result[0])
                result[0] = receive_array[i];
            if (receive_array[i] > result[1])
                result[1] = receive_array[i];
        }

        // printf("[SLAVE] Maior: %f e Menor: %f\n", result[1], result[0]);

        MPI_Send(result, 2, MPI_FLOAT, 0, 0, MPI_COMM_WORLD);
    }


    // MASTER
    if (meurank == 0)
    {
        float received_result[2];
        float result[2] = {MAX, 0};

        // Encontrando menor e maior valor entre todos os pacotes
        for (int i = 1; i < size; i++)
        {
            MPI_Recv(received_result, 2, MPI_FLOAT, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

            if (received_result[0] < result[0])
                result[0] = received_result[0];
            if (received_result[1] > result[1])
                result[1] = received_result[1];

            printf("Partial Response =  %f e %f\n", received_result[0], received_result[1]);
        }
        printf("\nRESULT \n");
        printf("[MASTER] Menor: e Maior:: %f e %f\n", result[0], result[1]);
    }

    MPI_Finalize();
}