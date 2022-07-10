# gRPC

* Framework en source de ROC para diversas linguagens
* Comunicação de serviços através de servidores e clientes
* Servidores são responsáveis em lidar com as chamadas dos clientes
* Clientes são stubs
* Usa o HTTP2 e Protobuff
- Ex de aplicações - comum em microsserviços, NETFLIX, SQUARE, CISCO

O gRPC foi criado como uma melhoria em uma arquitetura de comunicação RPC. O RPC é um modelo de comunicação entre dois processos dentro de um mesmo sistema operacional.

A ideia base do gRPC era ser muito mais perfornático do que a sua contraparte REST, por ser baseado no HTTP/2 e utilizar uma Linguagem de Definição de Interfaces (IDL) conhecida como Protocol Buffers(protobuf). Este conjunto de ferramentas torna possível que o gRPC seja utilizado em diversas linguagens ao mesmo tempo com um overhead muito baixo enquanto continua sendo mais rápido e mais eficiente do que as demais arquiteturas de chamadas de rede

## Funcionalidades
- Chamadas de procedimento remoto em lote
- Chamadas de procedimento em broadcast
- procedimentos de call-back
- Múltiplos requests em uma única conexão TCP
- Permite o sincronismo/assincronismo e a persistência na comunicação

## Arquitetura
Arquitetura Cliente/Servidor em que do lado de Servidor temos uma camada de **skeleton**(decriptador de uma chamada de rede para uma chamada de função) responsável em chamar a função do lado do servidor.

Enquanto isso, do lado do Cliente, temos uma chamada de rede feita por um stub, que é como um "falso" objeto representando o objeto do lado do servidor. Este objeto tem todos os métodos com suas assinaturas.

Ou seja, temos um cliente que converte as chamadas feitas localmente em chamadas de rede binárias com o protobuf e as envia pela rede até o servidor gRPC que as decodifica e responde para o cliente.


## HTTP2
- Está implicito no gRPC
- Redução de latência
- Minimização da carga do protocolo
- Adição de suporte a priorização de solicitação

Ele é muito mais rápido que o HTTP/1.1 por conta de vários fatores:

1. Multiplexação de requests e respostas

Nele é possível enviar várias chamadas e receber várias respostas em uma mesma conexão, coisa que não é possível no HTTP/1.1 que recebe e envia apenas uma requisição/resposta por vez. 
Isso é possível por causa da criação de um novo frame no pacote HTTP -> **Binary Framming**

O **Binary Framming** separa as duas partes (headers e payload) da mensagem em dois frames separados, porém contidos na mesma mensagem dentre de um encoding específico.

2. Compressão de Headers
Utilizando uma técnica chamada HPack, o HTTP/2 consegue mapear os headers de cada lado da chamada e verificar se foram alterados. É enviado então somente os headers que tiveram alguma mudança, e os que não foram recebem um índice para o valor anterior do header, evitando que headers sejam enviados repetidamente.


## Protocol Buffer
- Mecanismo extensível de serialização de dados estruturados
- Maneira de especificar um arquivo de definição de interface

ProtoBuf                                            JSON
Necessita de manos largura de banda                 Necessita de mais largura de banda
Escrito em binário                                  Escrito em formato textual legível

É um método de serialização e desserialização de dados que funciona através de uma IDL.
Ele é agnóstico de plataforma, então você pode escrever a especificação e uma linguagem neutra e compilar esse contrato para outros vários serviços. (Linguagem única de contrato entre serviços)

O protobuf em si não contém nenhuma funcionalidade, ele é apenas um descritivo de um serviço. O serviço no gRPC é um conjunto de métodos, pense nele como se fosse uma classe. Então podemos descrever cada serviços com seus parâmetros, entradas e saídas.

Cada método (ou RPC) de um serviço só pode receber um único parâmetro de entrada e um de saída, por isso é importante podermos compor as mensagens de forma que elas formem um único componente.

Além disso, toda mensagem serializada com o protobuf é enviada em formato binário, de forma que a sua velocidade de transmissão para seu receptor é muito mais alta do que o texto puro, já que o binário ocupa menos banda e, como o dado é comprimido pelo HTTP/2, o uso de CPU também é muito menor.

## Vantagens
- Mais leve e mais rápido por utilizar codificação binária e HTTP/2
- Multi plataforma com a mesma interface de contratos
- Funciona em muitas plataformas com pouco ou nenhum overhead
- O código é auto documentado
- Implementação relativamente fácil depois do desenvolvimento inicial
- Excelente para trabalhos entre times que não vão se encontrar, principalmente para definir contratos de projetos open source.

## Desvantagens
- O protobuf não possui um package manager para poder gerenciar as dependências entre arquivos de interface
- Exige uma pequena mudança de paradigma em relação ao modelo ReST
- Curva de aprendizado inicial é mais complexa
- Não é uma especificação conhecida por muitos
- Por conta de não ser muito conhecido, a documentação é esparsa
- A arquitetura de um sistema usando gRPC pode se tornar um pouco mais complexa




# Outro RPC: Java RMI (Remote Method Invocation)
Paradigma de comunicação através do qual objetos de processos diferentes podem comunicar-se uns com os outros. Extensçao de software à maquina Java remota (JVM) que permite, sintaticamente a invocação de métodos.
- Aplicações Cliente-Servidor
- Os stubs são os skeleton e o cliente é o proxy

