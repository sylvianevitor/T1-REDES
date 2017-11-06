# Echo client program
import socket
import subprocess
import string
import struct
from struct import *
import io

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria clientsocket
s.connect((HOST, PORT))				#estabelece conexao TCP: ip + porta do servidor

msg = "Funcionou"
typeOfService = 0
aux = io.BytesIO(bytes(0))

header = io.BytesIO()
#conteudo = (aux)
header.write(struct.pack('!H', typeOfService))


# 3 - way handshake acontece por baixo dos panos
s.sendall(bytes(msg.encode('utf-8'))) #envia mensagem via clientsocket
data = s.recv(1024)			#aguarda resposta do servidor e coloca em data
s.close()					#fecha socket e conexao TCP
print ('Received ')
print(repr(data))