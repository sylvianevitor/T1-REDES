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
typeOfService = 4  #OBS: Se >65535 mudar stuct.pack('H', ...)
arg2 = 3
msg = "df"
parametro = bytes(msg.encode('utf-8'))


header = io.BytesIO()
#conteudo = (aux)
header.write(struct.pack('!H', typeOfService ))
pacoteB = bytes


pacoteB = (struct.pack('hh255p', typeOfService, arg2, parametro))

conversor = bytes(header)

# 3 - way handshake acontece por baixo dos panos
s.sendall(pacoteB) #envia mensagem via clientsocket
data = s.recv(1024)			#aguarda resposta do servidor e coloca em data
saida = struct.unpack('255p', data)
s.close()					#fecha socket e conexao TCP
print ('Received ')
result = saida[0].decode('utf-8')
print(result)