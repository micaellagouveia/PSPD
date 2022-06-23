#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <math.h>
#define PORT 8080
#define MAX 500000

float f_aleat() {
    float random = rand()%MAX + 1;
    return random;
}

int main(int argc, char const* argv[])
{
    int sock = 0, valread, client_fd;
    struct sockaddr_in serv_addr;
    char buffer[1024] = { 0 };
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }
 
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
 
    // Convert IPv4 and IPv6 addresses from text to binary
    // form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }
 
    if ((client_fd = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }

    // Generate vetor
    float vetor[MAX];

    for(int i = 0; i < MAX; i++){
        vetor[i] = f_aleat();
        float tmp = vetor[i];
        //printf("NÚMERO: %.2f\n", tmp);
        vetor[i] = sqrt(tmp);
        //printf("NÚMERO COM RAIX: %.2f\n", vetor[i]);
        
        send(sock, &vetor[i], sizeof(float), 0);
        printf("[Client] Enviado: %.2f\n", vetor[i]);
    }
    
    valread = read(sock, buffer, 1024);
    printf("%s\n", buffer);
 
    // closing the connected socket
    close(client_fd);
    return 0;
}