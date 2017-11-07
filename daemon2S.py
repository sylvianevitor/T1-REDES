import socket
import struct
from struct import *
import subprocess
import string
import io

HOST = ''  # Qualquer host
PORT = 9002  # Porta arbitraria
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

    cmd = pacote[8]
    # Comando a ser executado

    if cmd == 1:
        print('Vai executar comando ps')
        var = "ps"

    elif cmd == 2:
        print('Vai executar comando df')
        var = "df"

    elif cmd == 3:
        print('Vai executar comando finger')
        var = "finger"

    elif cmd == 4:
        print('Vai executar comando uptime')
        var = "uptime"


    arg = pacote[12].decode('utf-8')  # opcoes de execucao

    if(arg != '0'):
        var = var + " " + arg  # concatena comando e opcoes


    proc = subprocess.Popen(var, stdout=subprocess.PIPE, shell=True)  # cria subprocesso para executar comando
    (saida, err) = proc.communicate()  # redireciona saida

    pacoteB = bytes
    pacoteB = (struct.pack('255p', saida))  # Monta pacote de volta
    print(saida)

    conn.sendall(pacoteB)  # Envia resposta, resultado da execucao
conn.close()  # Fecha socket e conexao TCP