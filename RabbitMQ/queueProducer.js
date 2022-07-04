// Work Queues
// Objetivo: Construir um Produtor que envia uma mensagem para uma fila. Analisar esse envio para vários
// consumidores para ver como a fila irá trabalhar com vários consumidores

const amqp = require('amqplib/callback_api');

// conectando conexão com o amqp
amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    // criando canal de conexão
    connection.createChannel((error1, channel) => {
        const queue = 'task_queue';
        const msg = process.argv.slice(2).join(' ') || "Hello World!";

        channel.assertQueue(queue, { durable: true });
        channel.sendToQueue(queue, Buffer.from(msg), { persistent: true });
        console.log(" [Producer] Sent '%s'", msg);
    });

    setTimeout(() => {
        connection.close();
        process.exit(0)
    }, 500);
})