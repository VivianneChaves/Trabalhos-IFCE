import socket, threading, json
from emprestimo import *

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

        while True:
            #Recebimento das variaveis
            data = self.csocket.recv(2048)
            vp = float(data.decode("UTF-8"))
            data1 = self.csocket.recv(2048)
            n = int(data1.decode("UTF-8"))



            #Intanciando a classe empréstimo e fazendo suas devidas funções
            e = Emprestimo(vp,n)
            vf = e.valor_final()
            vparc = e.valor_parc()
            je = e.juros_efetivo()

            #Colocando as variáveis em uma lista e enviando para o client a partir do método dumps
            dataf = [vf, vparc, je]
            dataf = json.dumps(dataf)
            self.csocket.send(dataf.encode('ascii'))

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
server.listen(1)
while True:
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()