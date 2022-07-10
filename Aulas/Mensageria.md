# Sistemas de Mensageria

- Aplicação Assínrona
- A mensagem possui metadados (cabeçalho, ...), ela possui a routingKey que é uma string que define a chave da rota.

## Modelos

### Ponto a ponto
Produtor sabe qual a fila que vai enviar e Consumidor sabe qual a fila que vai consumir. Quando o Consumidor recebe a mensagem, ele avisa o Produtor que ele recebeu a mensagem. Os dois têm conhecimento um do outro.

### Tópicos
de fato implementam o Publish/Subscribe. Não há a necessidade de ter uma fila, mas ela facilita. O Produtor publica mensagens em tópicos e o Consumidor pode se interessar por esses tópicos. Produtor e Consumidor não se conhecem.

## Protocolos

- AMQP *
- MQTT *
- STOMP *: Voltado para strings/texto (HTTP)
- ActiveMQ: Java

ESTUDAR *

### AMQP - Advanced Message Queue Protocol
Protocolo avançado de gerenciamento de filas

Componentes:
- Exchanges: ponto de registro, faz uma espécie de roteamento das mensagens para as filas
- Queues
- Bindings: regra de conexão, uma ligação que obedece um critério definido. É o que determina a ligação da exchange com a fila (regra da routingKey)
