# Comunicação

As camadas física de enlace dizem respeito ao hardware, já as camadas de rede e transporte estão embutidas no sistema operacional. Já as camadas de sessão, apresentação e aplicação são mais alto nível.

camada de sessão -> gerência de diálogo.


## Middlewares
Entre as camadas de transporte e a de aplicação
Mais alto nível que os sockets, assim vc não precisa usar os sockets daquela forma.

## Stubs
Faz a conversão dos tipos de dados entre uma máquina e outra, possibilitando a conexão com chamadas de procedimento remoto.

* passagem de valores por parâmetro.
* RPC assíncrono
* O rpc é um middleware simplificado

## Persistência e Sincronicidade
A comunicação entre dois nós pode ser persistente ou não, síncrono ou não.
Persistência é continuar ativo independente dos interesses dos hosts.

Existem alguns cenários
1. Host A e B conectados, canal de comunicação ATIVO
2. Host A conectado, Host B não conectado, canal de comunicação ATIVO
2. Host B conectado, Host A não conectado, canal de comunicação ATIVO
3. Hosts não conectados, canal de comunicação ATIVO. Ex: Emails usando SMTP. Fila de mensagens

## Integração e Interoperabilidade
1. O sistema está integrado quando todas as suas partes conseguem se comportar como um.
2. Ações entre os sistemas. Depende de dois requisitos
    * Padrão de Mensagem
    * Protocolo de Comunicação



