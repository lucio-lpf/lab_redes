import socket
import time
import sys


if len(sys.argv) is not 3:
    print("Chamamento errado. Por favor, utilize o modelo:\n python cliente.py ip_servidor porta_servidor")
    exit()
HOST = sys.argv[1]
PORT = int(sys.argv[2])
send = ['a']*64000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)

print 'Para sair use CTRL+X\n'

while True:
    tcp.send (','.join(send))

tcp.close()
