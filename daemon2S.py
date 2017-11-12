import socket
import struct
from struct import *
import subprocess
import string
import io
import math

#ESTABELECER CONEXAO TCP
HOST = ''  # Qualquer host
PORT = '8002'  # Porta arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria welcomesocket IPV4, TCP
s.bind((HOST, int(PORT)))  # Aguarda requisicao na welcome socket
s.listen(1)  # Aguarda requisicao na connection socket
conn, addr = s.accept()  # Cria connection socket quando recebe requisicao
print('Connected by ')
print(addr)


#fazer checksum

while 1:
    #RECEBIMENTO DE PACOTE
    data = conn.recv(785)  # Recebe mensagem na connection socket
    if not data: break

    #DESCOMPACTACAO DO CABECALHO 
    pacote = bytes
    pacote = struct.unpack('hhhhhhhhhh255p255p255p', data)
    print(pacote)

    #VERIFICACAO DO COMANDO A SER EXECUTADO
    if pacote[8] == 1:
        print('Vai executar comando ps')
        protocol = "ps"
    elif pacote[8] == 2:
        print('Vai executar comando df')
        protocol = "df"
    elif pacote[8] == 3:
        print('Vai executar comando finger')
        protocol = "finger"
    elif pacote[8] == 4:
        print('Vai executar comando uptime')
        protocol = "uptime"

    #VERIFICACAO DA OPCAO DE EXECUCAO
    opt = pacote[12].decode('utf-8')  # opcoes de execucao
    if(opt != '0'):
       if (("<" in opt) & (">" in opt) & ("|" in opt)):   #ha parametros maliciosos
            conn.close()    
       protocol = protocol + " " + opt  # concatena comando e opcoes

    #CRIACAO DAS THREADS POR REQUISICAO
    proc = subprocess.Popen(protocol, stdout=subprocess.PIPE, shell=True)  # cria subprocesso para executar comando
    (saida, err) = proc.communicate()  # redireciona saida

    qtd = math.ceil(len(saida) / 255)  # teto do tamanho da saida / max de bytes que podem ser enviados

    #MONTAR RESPOSTA
    pacoteB = bytes
    vers = pacote[0]
    ihl = pacote[1]
    tsV = pacote[2]
    tam = pacote[3]  #tamanho total do pacote
    idt = pacote[4]
    fl = 111 #resposta
    fgoff = pacote[6]
    time = pacote[7] - 1 #decrementa ttl
    prot = pacote[8]
    hCheck = pacote[9]
    srcAd = pacote[11]  # inverte source address/destination address
    dAd = pacote[10]
    opt = 0


    #ENVIAR PACOTES COM PEDACOS DO DADO 
    for i in range (0,qtd + 1):
        payld = saida[:255]
        saida = saida[255:len(saida)]
        pacoteB = (struct.pack('hhhhhhhhhh255p255ph255p', vers, ihl, tsV, tam, idt, fl, fgoff, time, prot, hCheck, srcAd, dAd, opt, payld))
        print(payld)
        print ("\n\n")
        conn.sendall(pacoteB)  # Envia resposta, resultado da execucao    

conn.close()  # Fecha socket e conexao TCP