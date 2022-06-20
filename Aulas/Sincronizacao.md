# Problema de Sincronização

- Como os processos se sincronizam entre si:
- Várias máquinas, vários relógios
    - Relógios Físicos
    - Relógios Lógicos
- Exclusão Mútua de execução
- Algoritmos eletivos
- Transações atômicas distribuídas

- Tempo global: A acontece antes de B
- Em um sistema distribuído, não há tempo global
- Não há uma fonte única de geração de tempo
- Isso dificulta obter conformidade em relação ao tempo

*É possível sincronizar todos os relógios de um sistema distribuído?*

## Relógios Físicos
- Serviço de sincronização de relógios físicos mais amplamente utilizado na internet: NTP (Network Time Protocol).
    - Precisão: 1 - 50 msec

## Relógios Lógicos
- Garante o tempo global, ou seja, que o A acontece antes de B. 
- Junto à mensagem, vai a referência de tempo do host
- Mexe nos clocks lógicos das máquinas 

