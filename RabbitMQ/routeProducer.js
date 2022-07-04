#!/usr/bin/env node

const amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    connection.createChannel((error1, channel) => {
        if (error1) throw error1;

        const exchange = 'direct_logs';
        const args = process.argv.slice(2);
        const msg = args.slice(1).join(' ') || 'Hello World!';

        // a severidade do log vai ser usada como a chave de roteamento para as filas
        const severity = (args.length > 0) ? args[0] : 'info';

        // criação da exchange do tipo direto
        channel.assertExchange(exchange, 'direct', { durable: false });

        // publicação da mensagem à exchange com sua chave de roteamento
        channel.publish(exchange, severity, Buffer.from(msg));

        console.log(" [Producer] Sent in route %s: '%s'", severity, msg);
    });

    setTimeout(() => {
        connection.close();
        process.exit(0);
    }, 500);
});

/*
Para rodar exemplo: node routeProducer.js error "Mensagem de erro" 
Para rodar exemplo: node routeProducer.js rota1 "Mensagem para rota1" 
*/