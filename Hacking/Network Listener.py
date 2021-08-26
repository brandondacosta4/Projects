  
# Basic network listener that listens for incoming connections. You can add code to be executed after the connection is successful 
import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip_address = input("IP Address: ")
port = input("Port: ")
listener.bind((ip_address, port))
listener.listen(0)
print("*** Waiting for incoming connections ***")
listener.accept()
print("*** Conection Successful *** ")

# Add code that will be executed after successful connection here
