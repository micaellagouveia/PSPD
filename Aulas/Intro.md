# Programação de Sistemas Paralelos e distribuídos
senha aprender: pspd2022.1

## Programação C/S usando RPC (Chamada de Procedimento Remoto)
Chamar e usar uma função que está em outra máquina.
Caracteriza-se por ser uma programação distribuída em várias máquinas.
Tem a função de garantir que uma variável possa ser acessada em diferentes máquinas, possuíndo uma notação interna, podendo ser também de diferentes sistemas operacionais.
é mais alto nível que os sockets
Fica acima da camada de transporte e do socket
É necessário instalar o ambiente para programação remota (rpcgen junto com IDF(interface))
- endereço loopback

É necessário um serviço de nomes que traduz as portas. O DNS é um serviço que faz a tradução para um endereço IP, já para o RPC é necessário tradução de portas.(Portmaps)

* Daemon - processo sem terminal anexado


Contras: 
* questões de segurança
    * identificação do requisitante


* Mecanismos de comunicação de interprocessos: mecanismos para comunicação entre processos de diferentes hosts
    * Ex: Pipes, filas de mensagem, shm, sockets TCP/UDP
    * Tudo isso foi visto em FSO e Redes

Processo é um programa em execução
    - área de texto (binário)
    - dados
    - "pilha"


## Diferença entre RPC e Serviços Web
- Geralmente para um web service, é necessário o uso de frameworks, que são um servidor que guardará os scripts da sua aplicação, o cliente entao acessa esse servidor para pode ter acesso a sua aplicaçãi

- Já no RPC, é necessário um middleware em cima da camada de TCP/UDP (Transporte)
    - Ex: RPC, RMI, gRPC, corba(mais sofisticado)
    Ele permite a criação de uma aplicação distribuída
    Uniao das máquinas, e o poder de processamento, capacidade, escalabilidade, disponibilidade será aumentado.

- O middleware geralmente pode ter:
    - Serviço de comunicação
    - Serviço de localização (Nomes)
    - Compilação

### IDF - Interface Definition File
Arquivo de definição de Interface (Ex: calcula.x) do RPC
Aplica-se também no RMI (o que muda o RPC para o RMI são os acessos)
Descrição das funçõe que serão criadas, variáveis que irão fluir de uma máquina para outra.
- Aplica-se o rpcgen, gera cliente e servidor, gerando também os stubs do cliente e do servidor

### Serviço de Nomes
Serviço de localização

- Funciona como um grafo, onde ele lê o caminho da esquerda para a direita, a / significa a aresta, e o nome é o nó.
Ex: /home/aluno/teste.c

Já no DNS, lê-se o caminho da direita para esquerda e o ponto é a aresta, e o nome o nó.
Ex: www.xpto.com.br

- Portmapper é uma tabela simples  ($ rpcinfo -p   - mostra a tabela)
função - porta
add - 8000
sub - 8001

Ele sempre está no mesmo host do Servidor, ele só traduz as portas da máquina do servidor.

- LDAP
É também um grafo que não tem a necessidade de escrever certinho o nome do endereço.
Funciona como um banco de dados mais voltado para leitura.
Um valor pode ser igual a outro. Ex: o = br, cm = campus, en = engenharia....


Relembrando...
### Escalonamento de Processos

Máquina de estados de Processos
- Fila de processos
- Processo pode estar na fila, em execuçao ou em espera


# Máquinas 
Multiprocessadores -> possuem mais de um cpu, compartilham memória.
                   -> Problema: há necessidade de manter a coerência da memória cache

Multicomputadres -> possuem mais de um host, cada um com um cpu distinto, não compartilham memória
                 -> Comunicação entre processos é feita via troca de mensagens
                 -> Esquema de messageria
                 -> Encapsula de forma que isso é uma coisa só

Contextos híbridos -> envolvem multiprocessadores e multicomputadores

Sistema distribuído multicomputador -> instala um mesmo sistema operacional em diferentes hosts, dando a impressão para o desenvolvedor de que é uma máquina só (**Sistemas fortemente acoplados - responsabilidade do SO em detectar os hosts**)

Sistema Operacional de rede -> há uma aplicação distribuída entre os hosts, mas eles são percebidos pelo desenvolvedor, ou seja os serviços de rede e middleware são separados por hosts e são percebidos.


Sistemas fracamente acoplados - Troca de responsabilidade de detecção para os middlewares. Ex: serviços de rede, compartilhamento de discos, impressoras ...

