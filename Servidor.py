import socket 
from PIL import Image
import os
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)


while True:
    conexao, endereco = server.accept()
    dados = conexao.recv(1024).decode('utf-8')
    mensagens = dados.split(";")
    operacao = mensagens[0]
    x = mensagens[1]
    y = mensagens[2] if len(mensagens) > 2 else False
    z = mensagens[3] if len(mensagens) > 3 else False
    k = mensagens[4] if len(mensagens) > 4 else False

    if operacao == "SOMA": resultado = float(x) + float(y)
    elif operacao == "SUBTRACAO": resultado = float(x) - float(y)
    elif operacao == "PRODUTO": resultado = float(x) * float(y)
    elif operacao == "DIVISAO":
        try:
            resultado = float(x) / float(y)
        except ZeroDivisionError:
            resultado = 0
    elif operacao == "QUADRADO": resultado = float(x) * float(x);
    elif operacao == "UPPERCASE": resultado = x.upper()
    elif operacao == "REDIMENSIONAR":
        img = Image.open(x) 
        img_redimensionada = img.resize((int(z), int(k)))
        img_redimensionada.save(y, format="PNG")
        resultado = os.path.getsize(y)
    else: resultado = 0
    conexao.sendall(str(resultado).encode('utf-8'))
    conexao.close()