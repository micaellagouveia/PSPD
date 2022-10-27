# BlockChain

- Conjunto de tecnologias
    - Criptografia de hash
    - Prova de trabalho

É uma espécie de banco de dados em que as negociações de bitcoins e outros ativos digitais ficam gravadas. Mas ela nao neessariamente se resume à compra ou venda de bitcoins ou criptomoedas.

O armazenamento dessas transações se dá em servidores descentralizados e distribuídos, ou seja, não ficam em um único lugar, e cada servidor, chamado de servidor de mineração, ele possui uma cópia do blockchain, e dentro do blockchain armazena-se os dados das transações.

Mineração: verificação dos blocos, gerando um hash.
Hash: operação criptográfica que gera identificadores únivos e irrepetíveis a partir de uma determinada informação. Hashes são uma peça chave da tecnologia blockchain

## Algoritmos de Consenso
Como o blockchain trabalha com um sistema distribuído e sem um MASTER, todos os nós(servidores) devem entrar em um consenso se a informação adicionada é valida ou não.

### Proof Of Work
Algoritmo que possibilita que todos os nós possuam a mesma cópia do banco de dados.

Como funciona:
Os mineradores tem o papel de validar se o novo bloco adicionado é valido, para isso, eles devem encontrar a solução de hash gerada. Essa hash não pode ser predita, apenas adivinhada. 
Demanda tempo encontrar uma solução válida, e quando vc encontra, vc prova que vc gastou tempo trabalhando para encontrar a solução, sendo concedido para o minerador um valor de bitcoin. 
Após  mineração, o bloco é adicionado na cadeia e é atualizado o banco de dados de todos os nós


## Hash Consistente
Usada para sistemas distribuídos, que possuem dados distribuídos. 

Ela é uma forma de armazenamento desses dados em diferentes servidores que está aberto a mudanças, sejam adições ou remoções de servidores.

Como funciona:
Ela usa uma mesma função de hash para mapear as chaves e os servidores, criando um anel de hashes.

Os servidores ficam mapeados, e as chaves entram no anel. Para descobrir a qual servidor a chave pertence, basta rodar em sentido horário a posição da chave para o primeiro servidor encontrado. 

Isso possiblita que caso um servidor seja adicionado ou caia, poucas chaves devem ser redistribuídas ao servidores.

Problemas:
Dependendo do mapeamento dos servidores, um servidor pode ficar sobrecarregado de chaves por cobrir um espaço maior no anel.

Quando um servidor é retirado, há sobrecarga para outro -> Uma solução é o uso de nós virtuais dos servidores.

Nós virtuais
Com nós virtuais, cada servidor lida com segmentos do anel, tornando a distribuição mais balanceada.

Aplicações que usam hash consistente:
- Amazon DynamoDB
- Apache Cassandra
- Google Load Balancer

## Aplicações que usam P2P

O Torrent é um tipo de tecnologia de compartilhamento de arquivos Peer-to-peer (do inglês par-a-par ou simplesmente ponto-a-ponto, com sigla P2P), na qual vários usuários podem se conectar e compartilhar seus arquivos, em vez de depender de um único site ou fonte para baixar os arquivos.

Um usuário pode não só baixar o arquivo da fonte direta, mas também de outros usuários do mesmo torrent, facilitando uma transferência e tornando mais suave entre os usuários. Cada um dos pares atua como um mini-servidor, o que reduz significativamente a carga da rede.

Para entender o processo P2P, é essencial esclarecer alguns termos.

Pares: Todos os usuários envolvidos no compartilhamento de arquivos por meio do compartilhamento P2P torrent são chamados de pares. Dizem que são colegas, desde que continuem compartilhando arquivos na rede.
Semeadores: Um usuário que está baixando um arquivo de um torrent e simultaneamente o carrega para ser usado por outros usuários é conhecido como semeador.]


## DHT
Tabela Hash distribuída -> segmenta uma tabela hash e a distribui

- Mapeia os nós de forma balanceada
- Possui uma tabela de roteamento para subconjntos
- Possui uma função de distância entre o nó e chave