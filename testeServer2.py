import socket
import struct
from struct import *
import subprocess
import string
import io

HOST = ''  # Qualquer host
PORT = 9005  # Porta arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria welcomesocket IPV4, TCP
s.bind((HOST, PORT))  # Aguarda requisicao na welcome socket
# conexaco TCP estabelecida
s.listen(1)  # Aguarda requisicao na connection socket
conn, addr = s.accept()  # Cria connection socket quando recebe requisicao
print('Connected by ')
print(addr)
while 1:
    data = conn.recv(1024)  # Recebe mensagem na connection socket
    if not data: break
    # print(data)

    # Descompacta cabecalho
    pacote = bytes
    pacote = struct.unpack('hhhhhhhhhh255ph255p', data)
    print(pacote)

    cmd = pacote[12].decode('utf-8')  # Comando a ser executado

    if 'ps' in cmd:
        print('Vai executar comando ps')
        cmd = "ps"
    elif 'df' in cmd:
        print('Vai executar comando df')
    elif 'uptime' in cmd:
        print('Vai executar comando uptime')

        # elif 'finger' in cmd:
        # 	printf('Vai executar comando finger')

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)  # cria subprocesso para executar comando
    (saida, err) = proc.communicate()  # redireciona saida

    pacoteB = bytes

    resposta = "retornou a mensagem"
    testeResposta = bytes(resposta.encode('utf-8'))

    print(testeResposta)

    #pacoteB = (struct.pack('255p', saida))
    pacoteB = (struct.pack('255p', testeResposta))  # Monta pacote de volta
    print(saida)

    conn.sendall(pacoteB)  # Envia resposta, resultado da execucao
conn.close()  # Fecha socket e conexao TCP