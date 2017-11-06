import socket       
import subprocess
import string
import struct
from struct import *
import io


HOST = ''                # Host qualquer
PORT = 50006             # Porta qualquer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria welcomesocket IPV4, TCP
s.bind((HOST, PORT))	  # Aguarda requisicao na welcome socket

# Conexaco TCP estabelecida

s.listen(1)				  # Aguarda requisicao na connection socket
conn, addr = s.accept()   # cria connection socket quando recebe requisicao
print('Conctado a  ')	  # host + porta
print (addr)

while 1:
    data = conn.recv(1024) #recebe mensagem na connection socket

    # Parsing do cabecalho: decodificacao
    aux = io.BytesIO(data) #transforma dado em tipo binario BytesIO
    buff = struct.unpack('!HH', aux.read(4)) # Desempacota mensagem recebida em formato: big endian unsigned short

    #Preencher campos
    field = buff[0] >> 8 #shift de 8 bits, pegar primeiro campo
    version = field >> 4 #shift de 4 bits, pegar version 
    ihl = field & 0x0f	 #ignorar 4 bits a esquerda, os que sobram sao ihl 
   
    #data = data.replace("REQUEST ","")
    #execucao
    if not data: break
    if '1' in repr(data):
    	print('Vai executar comando ps')
    	cmd = "ps aux"
    	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)  #cria subprocesso para executar comando
    	(saida, err) = proc.communicate()    

    elif 'df' in repr(data):
    	print('Vai executar comando df')
    	proc = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True)  #cria subprocesso para executar comando
    	(saida, err) = proc.communicate()

    elif 'uptime' in repr(data):
    	print('Vai executar comando df')
    	proc = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True)  #cria subprocesso para executar comando
    	(saida, err) = proc.communicate()  

    #preencher cabecalho

    header_bytes = io.BytesIO()
    byte = ((self.version << 4) | self.ihl) << 8 
    header_bytes.write(struct.pack('!H', byte))

    conn.sendall(saida)		#envia resposta
    #print(repr(data))
conn.close()				#fecha socket e conexao TCP
