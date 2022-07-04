// Hello World
// Objetivo: Construir um Consumidor qye espera e recebe uma mensagem de Hello Worl#!/usr/bin/env node

const amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;

    connection.createChannel((error1, channel) => {
        if (error1) {
            throw error1;
        }

        const queue = 'Fila';

        channel.assertQueue(queue, { durable: false });

        console.log(" [Consumer] Waiting for messages in %s. To exit press CTRL+C", queue);

        channel.consume(queue, msg => {
            console.log(" [Consumer] Received %s", msg.content.toString());
        }, {
            noAck: true
        });
    });
});