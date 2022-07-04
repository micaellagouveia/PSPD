// Routing
// Objetivo: Criar rotas para as exchanges e filas

const amqp = require('amqplib/callback_api');

var args = process.argv.slice(2);

if (args.length == 0) {
    console.log("Usage: routeProducer.js [info] [warning] [error]");
    process.exit(1);
}

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    connection.createChannel((error1, channel) => {
        if (error1) {
            throw error1;
        }
        const exchange = 'direct_logs';

        channel.assertExchange(exchange, 'direct', { durable: false });

        channel.assertQueue('', { exclusive: true }, function (error2, q) {
            if (error2) throw error2;

            console.log(' [Consumer] Waiting for logs. To exit press CTRL+C');

            // Para cada nivel de severidade é criada uma ligação da exchange com a fila
            args.forEach(severity => {
                channel.bindQueue(q.queue, exchange, severity);
            });

            channel.consume(q.queue, msg => {
                console.log(" [Consumer] Rota %s: '%s'", msg.fields.routingKey, msg.content.toString());
            }, {
                noAck: true
            });
        });
    });
});

/*
Para rodar exemplo: node routeConsumer.js info warning error
Para rodar exemplo: node routeConsumer.js rota1 rota2 rota3
*/