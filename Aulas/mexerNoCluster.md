1. entrar na máquina via ssh
    - login e senha
    - é possível cadastrar uma chave para nao ficar colocando senha toda hr

2. ```ssh cm1```



A chococcino utiliza rpc pra se comunicar entre suas máquinas e possui um sistema de arquivo NFS

## Sistema de arquivo NFS
Ele é para Cliente/Servidor usando RPC (usa portmapper)
Sistema de arquivo distribuído
NFS Server/Client - possibilita que uma partição do disco de uma máquina possa ser visível para outra máquina
Uma máquina exporta a partição desejada e outra monta(mount) a partição (acessa a partição da outra máquina)

Por isso o chococcino possui 7 máquinas que compartilham o diretório home
É o mesmo disco para todas as máquinas, mas o processamento pode ser feito separadamente

LVM - logic volume -> ESTUDAR SOBRE

## Para particularizar o acesso do disco nas máquinas
Basta adicionar o seguinte código no .bashrc:
```
EXPORT HOME= ${HOME}/${HOSTNAME} --> usr/home/{cm1}
cd $HOME
```

baixar hadoop no chococcino, depois dar um link simbólico para as máquinas
```ln -s hadoop_raiz hadoop_maquina```


