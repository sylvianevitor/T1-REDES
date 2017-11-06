# Echo client program
import socket

HOST = '192.168.0.109'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria clientsocket
s.connect((HOST, PORT))				#estabelece conexao TCP: ip + porta do servidor

msg = "1"

# 3 - way handshake acontece por baixo dos panos
s.sendall(bytes(msg.encode('utf-8'))) #envia mensagem via clientsocket
data = s.recv(1024)			#aguarda resposta do servidor e coloca em data
s.close()					#fecha socket e conexao TCP
print ('Received ')
print(repr(data))