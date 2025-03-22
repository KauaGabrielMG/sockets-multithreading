import socket
import threading
import re

class ServidorCalculadora:
    def __init__(self, host='localhost', porta=5000):
        self._host = host
        self._porta = porta
        self._socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket_servidor.bind((self._host, self._porta))
        self._clientes_conectados = 0

    def iniciar(self):
        self._socket_servidor.listen(5)
        print(f"Servidor iniciado em {self._host}:{self._porta}")

        while True:
            socket_cliente, endereco = self._socket_servidor.accept()
            self._clientes_conectados += 1
            print(f"Cliente conectado: {endereco}. Total de clientes: {self._clientes_conectados}")

            thread_cliente = threading.Thread(target=self._processar_cliente, args=(socket_cliente, endereco))
            thread_cliente.daemon = True
            thread_cliente.start()

    def _processar_cliente(self, socket_cliente, endereco):
        try:
            while True:
                dados = socket_cliente.recv(1024).decode('utf-8')
                if not dados:
                    break

                print(f"Recebido de {endereco}: {dados}")
                resultado = self._calcular(dados)
                socket_cliente.send(str(resultado).encode('utf-8'))

        except Exception as e:
            print(f"Erro ao processar cliente {endereco}: {e}")
        finally:
            socket_cliente.close()
            self._clientes_conectados -= 1
            print(f"Cliente desconectado: {endereco}. Total de clientes: {self._clientes_conectados}")

    def _calcular(self, expressao):
        expressao = expressao.strip()

        try:
            if re.match(r'^[\d\+\-\*/\.\(\)\s]+$', expressao):
                return eval(expressao)
            else:
                return "Expressão inválida"
        except Exception as e:
            return f"Erro: {e}"

if __name__ == "__main__":
    servidor = ServidorCalculadora()
    servidor.iniciar()
