// Topic
// Objetivo: receber mensagens para a exchange com chaves de tópicos

const amqp = require('amqplib/callback_api');

var args = process.argv.slice(2);

if (args.length == 0) {
    console.log("Usage: topicProducer.js <facility>.<severity>");
    process.exit(1);
}

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    connection.createChannel((error1, channel) => {
        if (error1) throw error1;

        const exchange = 'topic_logs';

        channel.assertExchange(exchange, 'topic', { durable: false });

        channel.assertQueue('', { exclusive: true }, (error2, q) => {
            if (error2) {
                throw error2;
            }
            console.log(' [Consumer] Waiting for logs. To exit press CTRL+C');

            // Dando bind nas exchanges com suas rotas(chaves)
            args.forEach(key => { channel.bindQueue(q.queue, exchange, key); });

            channel.consume(q.queue, msg => {
                console.log(" [Consumer] %s:'%s'", msg.fields.routingKey, msg.content.toString());
            }, {
                noAck: true
            });
        });
    });
});

/*
Exemplos de uso:
node topicConsumer.js "kern.*"
node topicConsumer.js "#"
node topicConsumer.js "*.critical"
node topicConsumer.js "kern.*" "*.critical"
*/