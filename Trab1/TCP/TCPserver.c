#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080
#define MAX 500000
int main(int argc, char const* argv[])
{
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = { 0 };
    float element = 0.0;
    float vetor[MAX];
    
 
    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
 
    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
 
    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    if ((new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0) {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    for(int i = 0; i < MAX; i++) {
        valread = read(new_socket, &element, sizeof(float));
        vetor[i] = element;
        printf("[Server] Recebido: %.2f\n", vetor[i]);
    }

    // Greater than Less than
    float maior = 0;
    float menor = 0;

    for(int i = 0; i < MAX; i++) {
        if (i == 0) {
        maior = vetor[i];
        menor = vetor[i];
        }
        if (vetor[i] > maior) {
        maior = vetor[i];
        }
        if (vetor[i] < menor) {
        menor = vetor[i];
        }
    }

    // printf("[SERVER] MAIOR: %.2f e MENOR: %.2f\n", maior, menor);
    sprintf(buffer, "[Server] MAIOR: %.2f e MENOR: %.2f\n", maior, menor);

    send(new_socket, buffer, strlen(buffer), 0);
   
    // closing the connected socket
    close(new_socket);
    // closing the listening socket
    shutdown(server_fd, SHUT_RDWR);
    return 0;
}