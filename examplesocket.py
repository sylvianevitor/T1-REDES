
# IPV4 , TCP
#server must perform the sequence socket(), bind(), listen(), accept()
#client only needs the sequence socket(), connect(). 
#server does not sendall()/recv() on the socket it is listening 
#on but on the new socket returned by accept()

# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 57766              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #cria welcomesocket IPV4, TCP
s.bind((HOST, PORT))	  # Aguarda requisicao na welcome socket
# conexaco TCP estabelecida
s.listen(1)				  # Aguarda requisicao na connection socket
conn, addr = s.accept()   # cria connection socket quando recebe requisicao
print ('Connected by'), addr
while 1:
    data = conn.recv(1024) #recebe mensagem na connection socket
    if not data: break	
    conn.sendall(data)		#envia resposta
conn.close()				#fecha socket e conexao TCP

# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 57766              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria clientsocket 
s.connect((HOST, PORT))				#estabelece conexao TCP: ip + porta do servidor 
# 3 - way handshake acontece por baixo dos panos
s.sendall('Hello, world') #envia mensagem via clientsocket
data = s.recv(1024)			#aguarda resposta do servidor e coloca em data
s.close()					#fecha socket e conexao TCP
print 'Received', repr(data)
