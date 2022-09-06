# MPI

Message Passing Interface
- Permite comunicação entre processos por meio de uma API de comunicação.
- Processos podem estar em computadores diferentes
    - gera tráfego de rede
    - modelo ideal é utilizar infimibend
- Arquitetura distribuída
- A memória é local aos proecssos para compartilhar com outros processos (tem que enviar para os outros)

- Todos os processos fazem parte de um GRUPO

## Grupo
Os processos fazem parte de um grpo. No jargão MPI é o comunicador. 
- Existe um grup geral qd vc inicializa o MPI, em que todos podem conversar com todos. Mas é possível criar grupos específicos para trafegar mensagens entre processos específicos.
- Os processos são identificados por um "rank" no grupo
    - Os processos podem ser executados localmente ou remotamente
    - Cada host pode executar mais de um processo.
    - É possível definir quem vai ser o mestre e quem vai ser o escravo.

### Infimibend
(substituto de ehternet - protocolo de camada física)
- Possui conexões de baixa latência e alta vazão (20Gbps por link)
- Diferente de ethernet (não compartilha o canal), pois o ethernet possui uma latência mais alta e pode gerar vazão de até 400Gbps.

### Clusters
- Grupo de computadores interligados em rede
- Compartilham recursos, como disco (armazenamento)
- Comunicação entre nós (cada pc) feita por algum sistema de rede.
    - gargalo passa ser a rede



