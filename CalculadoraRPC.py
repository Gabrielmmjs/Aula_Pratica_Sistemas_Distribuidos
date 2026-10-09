import socket

class CalculadoraRPC:

    def __init__(self, ip_servidor: str, porta_servidor:int):
        self.ip_servidor = ip_servidor
        self.porta_servidor = porta_servidor


    def _realizarConexao(self, operacao:str, *args):
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         sock.connect((self.ip_servidor,self.porta_servidor))
         parametros = ";".join(str(valor) for valor in args)
         mensagem = f"{operacao};{parametros}"
         sock.sendall(mensagem.encode('utf-8'))
         resposta = sock.recv(1024).decode('utf-8')

         return resposta

    
    def soma(self, x:float, y:float):
        return self._realizarConexao("SOMA", x, y)

    def subtracao(self, x:float, y:float):
        return self._realizarConexao("SUBTRACAO", x, y)

    def produto(self, x:float, y:float):
        return self._realizarConexao("PRODUTO", x, y)

    def divisao(self, x:float, y:float):
        return self._realizarConexao("DIVISAO", x, y)

    def quadrado(self, x:float):
        return self._realizarConexao("QUADRADO", x)

    def upperCase(self, x:str):
        return self._realizarConexao("UPPERCASE", x)

    def redimensionar_imagem(self, path_img_origin:str, path_img_dest:str, widht:int, height:int):
        return self._realizarConexao("REDIMENSIONAR", path_img_origin,path_img_dest,widht,height)


if __name__ == "__main__":
    calculadora = CalculadoraRPC("127.0.0.1", 8080)
    print(calculadora.soma(3,4))
    print(calculadora.produto(3,4))
    print(calculadora.produto(3,4))
    print(calculadora.soma(-0.0,0.0))
    print(calculadora.divisao(4,0.0))
    print(calculadora.produto(1000000,1000000))
    print(calculadora.quadrado(20))
    print(calculadora.quadrado(0.5))
    print(calculadora.upperCase("oi, eu sou gabriel"))
    print(calculadora.upperCase("caraca muleke"))
    print(calculadora.upperCase("s"))
    print(calculadora.upperCase("1"))
    print(calculadora.upperCase("Como outros usuários deste dispositivo não terão acesso à sua atividade, você pode navegar com mais privacidade. Isso não muda como os dados são coletados pelos sites que você acessa e pelos serviços que eles usam, incluindo o Google. Os itens da Lista de Leitura, os downloads e os favoritos ficarão salvos."))
    print(calculadora.redimensionar_imagem(r"C:\Users\Aluno\Documents\GabrielMoraes\teste.jpg", r"C:\Users\Aluno\Documents\GabrielMoraes\teste_redimensionada2.png", 400, 400))
    print(calculadora.redimensionar_imagem(r"C:\Users\Aluno\Documents\GabrielMoraes\teste.jpg", r"C:\Users\Aluno\Documents\GabrielMoraes\teste_redimensionada3.png", 1000, 900))
    





     