import socket
import struct
from struct import *
import subprocess
import string
import io
import math
import sys
import threading

#ESTABELECER CONEXAO TCP
HOST = ''  # Qualquer host
PORT = '9001'  # Porta arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria welcomesocket IPV4, TCP
s.bind((HOST, int(PORT)))  # Aguarda requisicao na welcome socket
s.listen(1)  # Aguarda requisicao na connection socket

#RECEBIMENTO DE PACOTE
def receive():   
    data = conn.recv(785)  # Recebe mensagem na connection socket
    if not data: conn.close()

    #DESCOMPACTACAO DO CABECALHO 
    pacote = bytes
    pacote = struct.unpack('hhhhhhhhhh255p255p255p', data)

    #VERIFICACAO DO COMANDO A SER EXECUTADO
    if pacote[8] == 1:
        protocol = "ps"
    elif pacote[8] == 2:
        protocol = "df"
    elif pacote[8] == 3:
        protocol = "finger"
    elif pacote[8] == 4:
        protocol = "uptime"

    #VERIFICACAO DA OPCAO DE EXECUCAO
    opt = pacote[12].decode('utf-8')  # opcoes de execucao
    if(opt != '0'):
       if (("<" in opt) & (">" in opt) & ("|" in opt)):   #ha parametros maliciosos
            conn.close()    
       protocol = protocol + " " + opt  # concatena comando e opcoes

    #CRIACAO DO SUBPROCESSO
    proc = subprocess.Popen(protocol, stdout=subprocess.PIPE, shell=True)  # cria subprocesso para executar comando
    (saida, err) = proc.communicate()  # redireciona saida

    #CALCULO DO CHECKSUM
    totalSum = 0
    for i in range (0, 10):
        totalSum += pacote[i]
    for i in range(10, 13):
        textoS = pacote[i].decode('utf-8')
        for i in textoS:
            totalSum += ord(i)
    if (not (totalSum & pacote[9])):   #checksum nao confere
        conn.close()

    #MONTAR RESPOSTA
    pacoteB = bytes
    vers = pacote[0]
    ihl = pacote[1]
    tsV = pacote[2]
    tam = pacote[3] + 2
    idt = pacote[4]
    fl = 111 #resposta
    fgoff = pacote[6]
    time = pacote[7] - 1 #decrementa ttl
    prot = pacote[8]
    hCheck = totalSum
    srcAd = pacote[11]  #inverte source address/destination address
    dAd = pacote[10]
    opt = 0     #zera opcoes de execucao

    #ENVIAR PACOTES COM PEDACOS DO DADO 
    while 1:
        payld = saida[:255]  #quebrar resultado em pedacos de 255
        saida = saida[255:len(saida)]
        pacoteB = (struct.pack('hhhhhhhhhh255p255ph255p', vers, ihl, tsV, tam, idt, fl, fgoff, time, prot, hCheck, srcAd, dAd, opt, payld))
        conn.sendall(pacoteB)  # Envia resposta, resultado da execucao 
        if not payld: break   
    conn.close()  # Fecha socket e conexao TCP

#CRIAR THREAD PARA ACEITAR REQUISICAO
while 1: 
    conn, addr = s.accept()  # Cria connection socket quando recebe requisicao
    try: 
        threading.Thread(receive(), (conn,))
    except Exception as exc:
        raise

