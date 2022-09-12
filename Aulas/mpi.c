#include <stdio.h>
#include <mpi.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv)
{

    MPI_Init(&argc, &argv); // inicia o MPI

    int meurank, group_size;

    MPI_Comm_rank(MPI_COMM_WORLD, &meurank);
    MPI_Comm_size(MPI_COMM_WORLD, &group_size);
    printf("Olá mundo %d: Tem rank %d e tamanho %d\n", getpid(), meurank, group_size);

    // esse vai ser o mestre
    if (meurank == 0)
    {
        for (int i = 1; i < group_size; i++)
        {
            int n = i * 10;
            MPI_Send(&n, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
            printf("MESTRE: Enviei %d para o rank %d\n", n, i);
        }
    }
    // estamos nos escravos aqui
    else
    {
        int recebido;
        MPI_Recv(&recebido, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("ESCRAVO (%d): recebeu %d\n", meurank, recebido);
    }
    
    MPI_Finalize(); // agarda a finalização de todos os processos para finalizar
}

/*
mpicc mpi.c -o mpi
mpirun ./mpi
mpirun -n 4 ./mpi - determina o número de processos

Saber o número dos processos não ajuda para criar uma arquitetura
master/slave - MPI_Comm_rank (determina o rank de um processo)
MPI_COMM_WORLD: comunicador global
MPI_Comm_size - retorna o tamanho do grupo (qtd de processos dentro de um grupo) -> se assemelha com a qtd de threads do openmp
MPI_Send - faz um sand básico
MPI_Send(o que vai ser mandado, qts vezes vai ser mandado, tipo, para quem vai ser mandado, tag, comunicador)
MPI_Recv -  recebe as mensagens
MPI_Recv(buffer, qtd elementos estou recebendo, tipo do elemento, quem eu quero receber, tag, comunicador, status)
MPI_ANY_SOURCE- pode receber de qlq um q esteja mandando
MPI_ANY_TAG- pode receber de qlq um q esteja mandando
*/