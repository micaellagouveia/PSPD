# Apache Spark

É um framework de código aberto pra computação distribuída. Provê uma interface para programação de clusters com paralelismo e tolerância a falhas.

## Computação distribuída
Sistema que interliga vários computadores, conseguindo um grande poder de processamento
Computadores ligados = clusters. Cada computador é um nó
Conceito de dividir para conquistar

## Estrutura de Processamento
Feito em memória para otimizar e acelerar as cargas de trabalho. Ele utiliza o RDD (Resilient Distributed Dataset). Eles são utilizados em memória e representam uma coleção de dados, são imutáveis e cada nova operação gera-se um novo RDD até que os dados sejam armazenados em disco.

## Estruturas de Dados do Spark
### RDD
- APIs de Baixo Nível
- Não é tão utilizada hoje, é mais usado para manipulação de dados brutos e não processados e dados não estruturados
- Resiliente e Distribuído
- Lista de itens imutável
- **Transformações**: Operações transformam um RDD em outro
- **Ações**: operações que retornam um valor ou que fazem algo
- Shuffle: envio de dados pela rede, é causado por operações que requerem um rearranjo de partições
- São divididos em partições
    - Pequenas farias com diferentes partes de um RDD
    - RDDs espalham os dados para múltiplos processos/nós
    - O número de partições controlam o valor máximo de paralelismo

### Dataframe
- Dataset -> É uma coleção distribuída de dados. Não necessita de tipificação das colunas. É tipificado em tempo de compilação
- Dataframe -> É um Dataset organizado em colunas nomeadas do tipo Row. Cada uma das suas colunas são tipificadas. É tipificado em runtime

API inspirada no Pandas


