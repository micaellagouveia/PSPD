# OpenMP

Modelo para programação paralela. Adiciona novas construções em algumas linguagens (Fortran, C, C++) -> gcc

## Modelo Fork-join
*Não confundir com a syscall fork()*

- Inicia com uma única thread
- Quando a thread inicial encontra uma construção paralela do OpenMP, um conjunto de thread é criado **(fork)**
- No final da região paralela, o conjunto de threads é finalizado **(join)** e continua com o fluxo simples de uma thread.

- fork: cria o conjunto de threads
- join: finaliza o conjunto de threads

## Pragmas
Anuncia que o OpenMP será utilizado.

```
#pragma omp parallel
```

### Comandos
```
gcc openMp.c -o openmp -fopenmp
./openmp
```

CFLAG = openmp

## Escolher quantidade de thread
*openMp1.c*

Muitas vezes não é vantajoso utilizar todos os núcleos do PC.
O pc possui pouco memória como cache, quanto mais o programa aproveitar o cache
melhor será.
Desses 8 núcleos, somente quatro são núcleos e os outros são hyper threads

```
OMP_NUM_THREADS=2 ./openmp
```

Muitos casos também é necessário rodar mais threads do que a quantidade de núcleos do PC, então é possível rodar mais que 8 threads

```
OMP_NUM_THREADS=20 ./openmp
```

Essa variável pode ser exportada para o shell
```
export OMP_NUM_THREADS=6
```

OBS = Existe uma função **omp_set_num_threads(int)**

## Paralelização de Laços (for) 
*openMp2.c*

- Construção: ```pragma omp for [cláusulas](opcional)```
- A ```parallel``` especifica uma região que deve ser executada em paralelo. Sem esta construção, o programa executará de forma sequencial. 
- A ```for``` espeifica que as iterações do laço serão feitas em paralelo. As iterações são distribuídas pelas threads existentes.
- Se o objetivo é paralelizar apenas um for, as construções podem ser unidas em uma única construção **```#pragma omp parallel for```**
- Você pode escalonar, definindo a quantidade que vai ser passada para cada thread:
    - Static:```#pragma omp parallel for schdule(static, 4)```, vai passar de 4 em 4 para cada thread.
    - Dynamic: ```#pragma omp parallel for schdule(dynamic, 4)```, até quatro no máximo
    - Auto

## Variáveis compartilhadas e privadas
*openMp3.c*

- Cláusula **SHARED**: especifica um conjunto de variáveis que são compartilhadas entre as threads
- Cláusula **PRIVATE**: especifica um conjunto de variáveis privadas. É um pouco contra ituitivo.
    - Os valores no início da região paralela são indefinidos
    - Se há uma variável definida antes da região de parallel, e vc especifica ela como privada na região, será feita uma cópia dela sem atribuição de valor na região e depois ela morrerá junto com o fim da região.
Por padrão:
1. Variáveis privadas: dentro do pragma
2. Variáveis compartilhadas: fora de pragmas

## Área Crítica
*openMp4.c*

Região que somente uma thread pode existir por vez.

- Construção: ```#pragma omp critical```

## Sections
*openMp5.c*

Cada section usa apenas uma thread que executa uma função específica.

- Construção: ```#pragma omp sections```
- Construção: ```#pragma omp section```

Se quiser rodar em paralelo com sections
```#pragma omp parallel section```

Obs: a região paralela só acaba quando todas as sessões acabarem!

## Outros
1. Barreiras: garante que todas as threads nao passem de um ponto específico. Ela trava todo mundo em uma região, e qd todas chegarem, ele continua
2. Break: cancelamento de threads

