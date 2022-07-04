# RabbitMQ

RabbitMQ é um mediador de mensagens, ou seja, ele aceita e encaminha mensagens.

* Produtor: Programa que envia mensagens
* Fila: onde se armazena as mensagens. Muitos produtores podem enviar mensagens que vão para uma fila e muitos consumidores podem tentar receber os dados de uma fila.
* Consumidor Programa que espera para receber as mensagens

## Reconhecimento de Mensagem
As redes não são confiáveis ​​e os aplicativos podem falhar no processamento de mensagens, portanto, o modelo AMQP 0-9-1 tem uma noção de reconhecimento de mensagens : quando uma mensagem é entregue a um consumidor, o consumidor notifica o broker , automaticamente ou assim que o desenvolvedor do aplicativo escolher. fazer isso. Quando as confirmações de mensagens estiverem em uso, um broker removerá completamente uma mensagem de uma fila somente quando receber uma notificação para essa mensagem (ou grupo de mensagens).

## Confirmação de Mesagem
- Após o broker enviar uma mensagem para um aplicativo (usando o método basic.deliver ou basic.get-ok ).
- Após o aplicativo enviar uma confirmação (usando o método basic.ack ).

A primeira escolha é chamada de modelo de reconhecimento automático, enquanto a segunda é chamada de modelo de reconhecimento explícito. Com o modelo explícito, o aplicativo escolhe quando é hora de enviar uma confirmação. Pode ser logo após receber uma mensagem, ou depois de persisti-la em um armazenamento de dados antes do processamento, ou após o processamento completo da mensagem (por exemplo, buscar com êxito uma página da Web, processá-la e armazená-la em algum armazenamento de dados persistente).

Se um consumidor falecer sem enviar uma confirmação, o corretor o entregará novamente para outro consumidor ou, se nenhum estiver disponível no momento, o corretor aguardará até que pelo menos um consumidor seja registrado na mesma fila antes de tentar a reentrega.



## Queues
As filas são usadas para distribuir as tarefas demoradas entre vários Workers. A ideia principal é evitar fazer uma task com muitos recursos imediatamente e ter que eseprar que ela seja conlcuída. Em vez disso, agendamentos uma task para ser feita mais tarde. Encapsulamos uma task como uma msg e enviamos para uma queue. Um processo de trabalho executado em segundo plano exibirá as tarefas e, eventualmente, executará o trabalho. Quando você executa muitos Workers, as tasks serão compartilhadas entre eles.

São declarado alguns atributos, como:
- Nome
- Durabilidade (se sobrevive à uma reinicialização do broker)
- Exclusividade (usado apenas por uma conexão e a fila será excluída quando a conexão for encerrada)
- Exclusão automática (a fila que teve pelo menos um consumidor é excluída quando o última consumidor cancela a inscrição)

## Publish/Subscribe
Objetivo de enviar mensagens  vários consumidores.
O Publisher não tem conhecimento de qual worker receberá sua mensagem e nem se essa mensagem chegará para alguem. Ele envia a mensagem para um Exchange, que fará o encaminhamento das mansagens para as respectivas filas

## Exchanges

Existem alguns tipos de Exchanges
- Direct: transmite as mensagens para os consumidores inscritos com sua chave de associação
- Topic: transmite as mensagens para os consumidores de acordo com os tópicos criados
- Headers: Uma mensagem é considerada correspondente se o valor do cabeçalho for igual ao valor especificado na vinculação.
- Fanout: transmite todas as mensagens que recebe para todas as filas que conhece

Além do tipo, são declarados vários atributos, como:
- Nome
- Durabilidade (se sobreivem ao reinício do broker)
- Exclusão automática (a exchange é excluída quando a última fila é desvinculada dele)

- Binds: Relação entre a Exchange e a Queue, conecta a exchange com a Queue

### Routing
Para poder fazer uma assinatura para recebimento das mensagens é necessário rotear o caminho.
Para fazer esse roteamento é necessário ter uma chave de associação entre exhange e queue.

- Chave direta: usada na exchange direta, sendo uma chave de nome normal
- Chave de tópico: usada na exchange de tópicos. É uma lista de como a chave pode ser escrita

Ex: A chave de animais que consiste em três palavras, uma sendo a velociadade, a segunda uma cor e a terceira uma espécie. ```<velocidade>.<cor>.<especie>```

Fora criados três binds
- Q1 com ```*.orange.*```: está interessado em todos os animais laranjas
- Q2 com ```*.*.rabbit```: está interessado em todos os coelhos
- Q2 com ```lazy.#```: está interessado em todos os animais preguiçosos

OBS: * substitui apenas uma palavra. Já o # pode susbstituir nenhuma ou várias. Ou seja, no caso de ter uma chave lazy.orange.male.rabbit, mesmo tendo 4 palavras, ele corresponde ao último bind e será entregue à segunda fila Q2.

## RPC
Nosso RPC funcionará assim:

1. Quando o Cliente é inicializado, ele cria uma fila de retorno de chamada exclusiva anônima.
2. Para uma solicitação RPC, o Cliente envia uma mensagem com duas propriedades: reply_to , que é definida como a fila de retorno de chamada e correlação_id , que é definida como um valor exclusivo para cada solicitação.
3. A solicitação é enviada para uma fila rpc_queue .
4. O trabalhador RPC (também conhecido como servidor) está aguardando solicitações nessa fila. Quando uma solicitação aparece, ele faz o trabalho e envia uma mensagem com o resultado de volta ao Cliente, usando a fila do campo reply_to .
5. O cliente aguarda dados na fila de retorno de chamada. Quando uma mensagem aparece, ela verifica a propriedade correlação_id . Se corresponder ao valor da solicitação, ele retornará a resposta ao aplicativo.

### Server
O código do servidor é bastante simples:

1. Como de costume, começamos estabelecendo a conexão e declarando a fila rpc_queue .
2. Declaramos nossa função fibonacci. Ele assume apenas uma entrada válida de inteiro positivo. (Não espere que este funcione para grandes números, é provavelmente a implementação recursiva mais lenta possível).
3. Declaramos um callback on_request para basic_consume , o núcleo do servidor RPC. É executado quando a solicitação é recebida. Ele faz o trabalho e envia a resposta de volta.
4. Podemos querer executar mais de um processo servidor. Para distribuir a carga igualmente em vários servidores, precisamos definir a configuração prefetch_count .

### Client
1. Estabelecemos uma conexão, canalizamos e declaramos um callback_queue exclusivo para respostas.
2. Assinamos o callback_queue , para que possamos receber respostas RPC.
3. O retorno de chamada on_response que foi executado em cada resposta está fazendo um trabalho muito simples, para cada mensagem de resposta ele verifica se a correlação_id é a que estamos procurando. Em caso afirmativo, ele salva a resposta em self.response e interrompe o loop de consumo.
4. Em seguida, definimos nosso método de chamada principal - ele faz a solicitação RPC real.
5. No método de chamada , geramos um número de correlação_id exclusivo e o salvamos - a função de retorno de chamada on_response usará esse valor para capturar a resposta apropriada.
6. Também no método call , publicamos a mensagem de requisição, com duas propriedades: reply_to e correlação_id .
7. No final, esperamos até que a resposta adequada chegue e devolvemos a resposta ao usuário.