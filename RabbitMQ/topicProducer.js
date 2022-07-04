// Topic
// Objetivo: mandar mensagens para a exchange com chaves de tópicos

const amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', (error0, connection) => {
  if (error0) throw error0;

  connection.createChannel((error1, channel) => {
    if (error1) throw error1;

    const exchange = 'topic_logs';
    const args = process.argv.slice(2);
    const key = (args.length > 0) ? args[0] : 'anonymous.info';
    const msg = args.slice(1).join(' ') || 'Olá Mundo!';

    channel.assertExchange(exchange, 'topic', { durable: false });
    channel.publish(exchange, key, Buffer.from(msg));
    console.log(" [Producer] Enviado com chave %s:'%s'", key, msg);
  });

  setTimeout(() => {
    connection.close();
    process.exit(0);
  }, 500);
});

/*
Exemplo de uso: node topicProducer.js "kern.critical"  "Um erro crítico de kernel"
*/