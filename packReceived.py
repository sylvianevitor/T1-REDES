import socket
import struct
from struct import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #cria welcomesocket IPV4, TCP
s.bind((HOST, PORT))	  # Aguarda requisicao na welcome socket
# conexaco TCP estabelecida
s.listen(1)				  # Aguarda requisicao na connection socket
conn, addr = s.accept()   # cria connection socket quando recebe requisicao
print('Connected by ')
print (addr)
while 1:
    data = conn.recv(1024) #recebe mensagem na connection socket
    if not data: break
    print(data)

    pacote =bytes

    pacote = struct.unpack('hh255p', data)
    print(pacote)

    msg = pacote[2]
    print(msg)

    conn.sendall(data)		#envia resposta
conn.close()				#fecha socket e conexao TCP