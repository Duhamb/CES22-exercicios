#!/usr/bin/env python

from socket import *
import threading

HOST = 'localhost' # or '127.0.0.1'
PORT = 8080
BUFSIZ = 1024

class ThreadedClient(object):
	def __init__(self):
		self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
		ADDR = (HOST, PORT)
		self.tcpCliSock.connect(ADDR)
		host=self.tcpCliSock.getsockname() #  print client host name
		print(host)
		threading.Thread(target = self.reading, args = ()).start()

	def sending(self):
		while True:
			data = (input()).encode('utf-8')
			if not data:
				break
			self.tcpCliSock.send(data)
		self.tcpCliSock.close()

	def reading(self):
		while True:
			msg = self.tcpCliSock.recv(BUFSIZ)
			if not msg:
				break
			print(msg.decode('utf-8'))

if __name__ == "__main__":
    ThreadedClient().sending()