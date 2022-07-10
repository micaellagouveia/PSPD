# Ambientes de Programação Distribuída

- É o que chamamos de sistema de nuvem
- paradigma MapReduce/Hadoop

## Linha do Tempo de Utilização
- Anos 60: computadores grandes
- Anos 70: clusters
- Anos 90: grids
- Final dos anos 90: P2P
- Anos 2000: Cloud -> explora escalabilidade usando réplica e consistência

## Diferença entre Clusters e Grid
- Clusters: mais de um servidor ligados entre si por meio de uma rede LAN de alta velocidade. Nível de acoplamento alto. Distância curta entre servidores, no mesmo espaço físico, e nível de transmissão muito alto.
    - Cluster de Alta Performance (High Performance)
    - Cluster de Alta Disponibilidade (High Avaiability): se um servidor cai, o outro assume. Necessita de uma máquina que guarda os endereços IP e faz a demanda de carga.

- Grids: Servidores/Clusters espalhados (Ex: um em BSB e outro em SP). Estão separadas por uma rede de longa de distância, taxa de transmissão mais baixa, nível de acoplamento baixo.
    - Aplicações BoT (Baf of Task): você consegue distribuir as tarefas e uma não compromete tanto a outra.


## Estratégias de Escalabilidade
- Vertical (Scale up): uso de uma máquina mais potente
- Horizontal (Scale out): uso de várias máquinas pequenas em conjunto

## Tipos de nuvens
- Aplicação
- Infraestrutura

## Mais sobre servidores...
- Precisam ser autorreguláveis e ter uma estretégia para falhas
- Os servidores, discos, rede, cabo podem falhar, então os dados precisam ser **distribuídos** entre nós e hacks apara evitar grandes perdas.
