#!/usr/bin/python3
""" Example Socket server to send data to client
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Request coming from {address}")
    clientSocket.send(bytes(':: I am almighty server ::', 'utf-8'))
    clientSocket.close()
