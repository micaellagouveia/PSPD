// Hello World
// Objetivo: Construir um Produtor que envia uma mensagem de Hello World para uma fila de mensagens

const amqp = require('amqplib/callback_api');

// conectando conexão com o amqp
amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    // criando canal de conexão
    connection.createChannel((error1, channel) => {
        const queue = "Fila";
        const msg = "Hello World!";

        // setando e mandando msg para a fila
        channel.assertQueue(queue, { durable: false });
        channel.sendToQueue(queue, Buffer.from(msg));

        console.log("[Producer] Sent " + msg);
    });

    setTimeout(() => {
        connection.close();
        process.exit(0)
    }, 500);
})