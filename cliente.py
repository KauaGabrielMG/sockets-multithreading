import socket

class ClienteCalculadora:
    def __init__(self, host='localhost', porta=5000):
        self._host = host
        self._porta = porta
        self._socket = None

    def conectar(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._socket.connect((self._host, self._porta))
            print(f"Conectado ao servidor {self._host}:{self._porta}")
            return True
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            return False

    def enviar_operacao(self, operacao):
        if not self._socket:
            print("Não conectado ao servidor")
            return None

        try:
            self._socket.send(operacao.encode('utf-8'))
            resultado = self._socket.recv(1024).decode('utf-8')
            return resultado
        except Exception as e:
            print(f"Erro na comunicação: {e}")
            return None

    def fechar(self):
        if self._socket:
            self._socket.close()
            print("Conexão fechada")

def main():
    cliente = ClienteCalculadora()
    if cliente.conectar():
        try:
            while True:
                operacao = input("Digite uma operação matemática (ou 'sair' para finalizar): ")
                if operacao.lower() == 'sair':
                    break

                resultado = cliente.enviar_operacao(operacao)
                if resultado:
                    print(f"Resultado: {resultado}")
        finally:
            cliente.fechar()

if __name__ == "__main__":
    main()
