import socket
import threading
from time import ctime

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print("%s:%s has connected." % address)
            #client.settimeout(60)
            client.send(("Bem-vindo ao chat! Digite o seu nome de usuário: ").encode('utf-8'))
            addresses[client] = address
            threading.Thread(target = self.listenToClient,args = (client,address)).start()            

    def listenToClient(self, client, address):
        size = 1024
        name = client.recv(size).decode('utf-8')
        clients[client] = name
        msg = "%s has joined the chat!" % name
        self.broadcast(msg)
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    strdata=data.decode('utf-8')
                    prefix = name + ": "
                    self.broadcast(strdata, prefix)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                print("Exception")
                return False

    def broadcast(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the clients."""
        for client in clients:
            client.send((prefix + msg).encode('utf-8'))

clients = {}
addresses = {}

if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()