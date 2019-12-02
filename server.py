import socket
import thread
import csv
from time import sleep
import sys


HOST = ''              # Endereco IP do Servidor
send = ['a']*64000
size = sys.getsizeof(','.join(send))
valued_readed = 0

if len(sys.argv) is not 2:
    print("Chamamento errado. Por favor, utilize o modelo:\n python server.py porta_servidor")
    exit()

PORT = int(sys.argv[1])

def print_result_thread():
    file_name = 'mesure_'+ str(PORT) + '.csv'
    with open(file_name,'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        old_value = 0
        time = 0
        while True:
            value = valued_readed
            row = [0,0]
            row[0] = time
            row[1] = value - old_value
            old_value = value
            writer.writerow(row)
            sleep(1)
            time += 1


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

thread.start_new_thread(print_result_thread,())

while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(size)
        if not msg: break
        valued_readed += sys.getsizeof(msg)
    print 'Finalizando conexao do cliente', cliente
    con.close()
