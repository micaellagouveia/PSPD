// Exchange
// Objetivo: Receber as mensagens vindas da fila que está conectada com a exchange Logs

const amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    connection.createChannel((error1, channel) => {
        if (error1) throw error1;

        const exchange = 'logs';

        // Declaração da exchange de logs
        channel.assertExchange(exchange, 'fanout', {durable: false});

        // Declaração da fila exclusiva daquela exchange
        channel.assertQueue('', { exclusive: true }, (error2, q) => {
            if (error2) throw error2;

            console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", q.queue);

            // Ligando a exchange com a fila (como é do tipo fanout, não é necessário chave)
            channel.bindQueue(q.queue, exchange, '');

            channel.consume(q.queue, msg => {
                if (msg.content) console.log(" [Consumer] %s", msg.content.toString());
            }, {
                noAck: true
            });
        });
    });
});