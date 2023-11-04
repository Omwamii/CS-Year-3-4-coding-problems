#!/usr/bin/python3
""" Example Socket server to send data to client
"""
import socket

# SOCK_STREAM -> TCP Connection, SOCK_DGRAM -> UDP Connection
# AF_INET -> Address family for IPv4
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 6060)) # bind socket to hostname & port
    s.listen()
    conn, address = s.accept()  # accept request from client process
    print(f"Request coming from {address}")
    conn.send(bytes(':: I am almighty server ::', 'utf-8'))
    # conn is closed automatically by using 'with' context manager
