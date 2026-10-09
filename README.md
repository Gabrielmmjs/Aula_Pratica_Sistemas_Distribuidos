# Trabalho Individual — Sistemas Distribuídos

## Sobre o projeto

Projeto desenvolvido para a disciplina de Sistemas Distribuídos, com o objetivo de implementar a comunicação entre cliente e servidor utilizando sockets TCP em Python e o conceito de RPC (Remote Procedure Call).

O cliente solicita a execução de operações ao servidor, que processa as requisições e retorna os resultados.

## Funcionalidades

- **Soma:** soma dois números.
- **Subtração:** subtrai dois números.
- **Multiplicação:** multiplica dois números.
- **Divisão:** divide dois números, tratando a divisão por zero.
- **Quadrado:** calcula o quadrado de um número.
- **Uppercase:** converte textos para letras maiúsculas.
- **Redimensionamento de imagens:** altera as dimensões de uma imagem utilizando a biblioteca Pillow e salva o resultado no caminho especificado.

## Tecnologias utilizadas

- Python 3
- Sockets TCP
- Biblioteca Pillow (PIL)

## Estrutura do projeto

- **Cliente:** implementa a classe `CalculadoraRPC`, responsável por enviar requisições ao servidor e receber respostas.
- **Servidor:** recebe as requisições, executa as operações solicitadas e retorna os resultados.

## Pré-requisitos

- Python 3 instalado.
- Biblioteca Pillow instalada.

Instale a dependência com o comando:

```bash
pip install Pillow
```

## Como executar

### 1. Iniciar o servidor

Em um terminal, execute:

```bash
python servidor.py
```

O servidor ficará aguardando conexões no endereço `127.0.0.1`, porta `8080`.

### 2. Executar o cliente

Em outro terminal, execute:

```bash
python cliente.py
```

**Observação:** substitua `servidor.py` e `cliente.py` pelos nomes reais dos arquivos, caso sejam diferentes.

## Funcionamento

A comunicação ocorre por meio do protocolo TCP. O cliente envia mensagens codificadas em UTF-8, utilizando o caractere `;` para separar a operação e seus parâmetros.

Exemplo de requisição:

```text
SOMA;3;4
```

Resposta do servidor:

```text
7.0
```

No redimensionamento de imagens, o cliente envia o caminho da imagem original, o caminho de destino, a largura e a altura desejadas. O servidor salva a imagem redimensionada e retorna o tamanho do arquivo em bytes.

## Objetivo acadêmico

Aplicar conceitos de Sistemas Distribuídos, arquitetura cliente-servidor, comunicação por sockets, troca de mensagens e execução remota de operações.

## Autor

Gabriel Moraes

Trabalho Individual — Sistemas Distribuídos.
