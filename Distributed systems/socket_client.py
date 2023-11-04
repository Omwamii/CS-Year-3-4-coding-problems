#!/usr/bin/python3
""" Create a client-socket communication between two proccesses
"""
import socket

with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 6060))
    message = s.recv(2048)

print(f"Response from server: {message}")
