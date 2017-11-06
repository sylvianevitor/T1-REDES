#Daemon:

#- aceita conexao socket: servidor
#- recebe IPV4
#- parsing do comando recebido:
#	protocol: 1,2,3,4
#- execucao do comando recebido
#- preenche cabecalho IPV4
#- retorna saida
#- multithread

#1.ps: mostra snapshot dos processos correntes
#2.df: mostra espaco disponivel no sistema de arquivos
#3.finger: mostra informações sobre os users
#4.uptime: diz por quanto tempo o sistema esteve rodando




# IPV4 , TCP
#server must perform the sequence socket(), bind(), listen(), accept()
#client only needs the sequence socket(), connect(). 
#server does not sendall()/recv() on the socket it is listening 
#on but on the new socket returned by accept()

# Echo server program
import socket
import subprocess

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50006              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #cria welcomesocket IPV4, TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))	  # Aguarda requisicao na welcome socket
# conexaco TCP estabelecida
s.listen(1)				  # Aguarda requisicao na connection socket
conn, addr = s.accept()   # cria connection socket quando recebe requisicao
print ('Connected by')
print (addr)
while 1:
    data = conn.recv(1024) #recebe mensagem na connection socket
    if not data: break	

    #parsing de data: http://scapy.readthedocs.io/en/latest/usage.html#starting-scapy
    #executa comando: fork, exec, thread e redireciona saida
    #if (data == '1')
    subprocess.call(['ps', '-aux'])
    #data = preenche cabecalho e dado com resultado da execucao: http://www.binarytides.com/raw-socket-programming-in-python-linux/ 
    conn.sendall(data)		#envia resposta
conn.close()				#fecha socket e conexao TCP


