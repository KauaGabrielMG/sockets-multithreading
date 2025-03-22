# Servidor de Cálculo Distribuído

Este projeto implementa um servidor de cálculo distribuído que utiliza sockets e multithreading em Python.

## Funcionalidades

- Servidor que aceita múltiplas conexões de clientes usando threads
- Processamento de operações matemáticas enviadas pelos clientes
- Retorno dos resultados calculados para os clientes
- Suporte para operações básicas (+, -, \*, /)

## Como Executar

1. Inicie o servidor:

```
python servidor.py
```

2. Inicie um ou mais clientes em terminais separados:

```
python cliente.py
```

3. Digite operações matemáticas no cliente e receba os resultados do servidor.

```
Digite uma operação matemática (ou 'sair' para finalizar): 2 + 3
Resultado: 5
```
