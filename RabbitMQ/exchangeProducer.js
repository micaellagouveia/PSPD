// Exchange
// Objetivo: Criar uma exchange de logs do tipo fanout 

const amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    connection.createChannel((error1, channel) => {
        if (error1) throw error1;

        const exchange = 'logs';
        const msg = process.argv.slice(2).join(' ') || 'Hello World!';

        //Criação da exchange de logs do tipo fanout não durável
        channel.assertExchange(exchange, 'fanout', {durable: false});

        // Publicação da mensagem na exchange criada
        channel.publish(exchange, '', Buffer.from(msg));
        console.log(" [Producer] Sent %s", msg);
    });

    setTimeout(() => {
        connection.close();
        process.exit(0);
    }, 500);
});