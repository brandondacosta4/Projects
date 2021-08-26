import socket


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


print("Welcome to the python port scanner\n")
target = str(input("Please enter your target ip address: "))
while(True):
    port = int(input("Please enter the port number you would like to scan: "))
    if((scan_port(port)  == False)):
        print("The chosen port is closed\n")
    elif((scan_port(port) == True)):
        print("The chosen port is open\n")
