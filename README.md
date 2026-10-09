Trabalho Individual — Sistemas Distribuídos
Sobre o projeto

Este projeto foi desenvolvido como trabalho individual da disciplina de Sistemas Distribuídos. O objetivo é implementar um sistema de comunicação entre cliente e servidor utilizando sockets TCP em Python, aplicando o conceito de RPC (Remote Procedure Call), ou chamada de procedimento remoto.

A aplicação permite que o cliente solicite a execução de diferentes operações ao servidor, que processa as requisições e retorna os resultados.

Funcionalidades

O sistema implementa as seguintes operações:

Soma: soma dois números.
Subtração: calcula a diferença entre dois números.
Multiplicação: multiplica dois números.
Divisão: divide dois números, tratando a divisão por zero.
Quadrado: calcula o quadrado de um número.
Uppercase: converte um texto para letras maiúsculas.
Redimensionamento de imagens: altera a largura e a altura de uma imagem utilizando a biblioteca Pillow e salva o resultado em um caminho definido pelo cliente.
Tecnologias utilizadas
Python 3: linguagem utilizada no desenvolvimento.
Socket: biblioteca para comunicação entre cliente e servidor por meio do protocolo TCP.
Pillow (PIL): biblioteca utilizada para manipulação e redimensionamento de imagens.
Estrutura do projeto

O projeto é composto por dois programas principais:

Cliente: contém a classe CalculadoraRPC, responsável por enviar requisições ao servidor e receber as respostas.
Servidor: recebe as requisições, identifica a operação solicitada, executa o processamento e devolve o resultado ao cliente.
Como executar
1. Instalar a dependência

Certifique-se de ter o Python 3 instalado e execute:

pip install Pillow

2. Iniciar o servidor

Execute o arquivo Python que contém o código do servidor:

python servidor.py


O servidor ficará aguardando conexões no endereço 127.0.0.1, porta 8080.

3. Executar o cliente

Em outro terminal, execute o arquivo do cliente:

python cliente.py


O cliente realizará chamadas para testar as operações implementadas e exibirá os resultados retornados pelo servidor.

Observação: cliente.py e servidor.py são nomes ilustrativos. Utilize os nomes reais dos arquivos presentes no repositório.
Funcionamento da comunicação

A comunicação entre os programas ocorre por meio de sockets TCP. As requisições são enviadas como mensagens de texto codificadas em UTF-8, com os parâmetros separados pelo caractere ;.

O funcionamento segue estas etapas:

O cliente monta uma mensagem com o nome da operação e seus parâmetros.
A mensagem é enviada ao servidor por meio de uma conexão TCP.
O servidor interpreta a requisição e executa a operação correspondente.
O resultado é convertido em texto e enviado de volta ao cliente.
O cliente recebe a resposta e a apresenta ao usuário.
Exemplo de requisição

Uma chamada para somar dois números pode gerar a seguinte mensagem:

SOMA;3;4


O servidor realiza a operação e retorna:

7.0


No caso do redimensionamento de imagens, o cliente informa o caminho da imagem original, o caminho de destino e as dimensões desejadas. O servidor realiza o processamento e retorna o tamanho do arquivo gerado, em bytes.

Objetivo acadêmico

O trabalho busca aplicar conceitos fundamentais de Sistemas Distribuídos, incluindo comunicação por rede, arquitetura cliente-servidor, troca de mensagens e execução remota de operações.

Autor

Gabriel Moraes

Trabalho individual — Disciplina de Sistemas Distribuídos.
