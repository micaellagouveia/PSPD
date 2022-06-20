### Trabalho 1 (explicação)
CLIENT (inicializa vetor) < -(socket) - > SERVIDOR(maior ou menos) - servidor será chamado de WORKER
CLIENT (inicializa vetor) < -(RPC) - > SERVIDOR(maior ou menos)

- melhorar performance - usando dois WORKERS
    - apresentar um quadro comparativo de performance

PROX LAB - GRPC


# gRPC

* Framework en source de ROC para diversas linguagens
* Comunicação de serviços através de servidores e clientes
* Servidores são responsáveis em lidar com as chamadas dos clientes
* Clientes são stubs
* Usa o HTTP2 e Protobuff
- Ex de aplicações - comum em microsserviços, NETFLIX, SQUARE, CISCO

## Funcionalidades
- Chamadas de procedimento remoto em lote
- Chamadas de procedimento em broadcast
- procedimentos de call-back
- Múltiplos requests em uma única conexão TCP
- Permite o sincronismo/assincronismo e a persistência na comunicação

## Protocol Buffer
- Mecanismo extensível de serialização de dados estruturados
- Maneira de escpecificar um arquivo de definição de interface

ProtoBuf                                                        JSON
Necessita de manos largura de banda                             Necessita de mais largura de banda
Escrito em binário                                              Escrito em formato textual legível


## HTTP2
- Está implicito no gRPC
- Redução de latência
- Minimização da carga do protocolo
- Adição de suporte a priorização de solicitação



# Java RMI (Rmote Method Invocation)
Paradigma de comunicação através do qul objetos de processos diferentes podem comunicar-se uns com os outros. Extensçao de software à maquina Java remota (JVM) que permite, sintaticamente a invocação de métodos.
- APlicações Cliente-Servidor
- Os stubs são os skeleton e o cliente é o proxy

