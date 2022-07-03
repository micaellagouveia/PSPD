# Persistência da Comunicação

A aplicação deve ser capaz de falar com uma infresestrutura que provê persistência, ou seja, um intermediário, chamado de Broker.

Ex: RabbitMQ, Kafka

## Paradigma: Publish/Subscribe

Publicação de uma mensagem em uma canal, e os interessados se conectam a esse canal.
Os brokers são implementadores de canais, e a aqueles que vão consumir, assinam esse canal para consumirem essas mensagem

