#!/usr/bin/python
import cgitb
import cgi
import socket
import subprocess
import string
import struct
from struct import *
import io

#cgitb.enable()
print("Content-Type: text/html;charset=utf-8\r\n\r\n")

#Cria instancia de FieldStorage
form = cgi.FieldStorage()


#Cadastro dos daemons
HOSTD = '127.0.0.1'
P1 = '8001'
P2 = '8002'
P3 = '8003'

daemon1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
daemon2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
daemon3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

daemon1.connect((HOSTD, int(P1)))
daemon2.connect((HOSTD, int(P2)))
daemon3.connect((HOSTD, int(P3)))


#3-Way handshake
print("webserver.py\n")

#Get data from fields
#ATRIBUTOS DA MAQUINA 1
cbxM1PS = form.getvalue('maq1_ps')
cbxM1DF = form.getvalue('maq1_df')
cbxM1FINGER = form.getvalue('maq1_finger')
cbxM1UPTIME = form.getvalue('maq1_uptime')

#ATRIBUTOS DA MAQUINA 2
cbxM2PS = form.getvalue('maq2_ps')
cbxM2DF = form.getvalue('maq2_df')
cbxM2FINGER = form.getvalue('maq2_finger')
cbxM2UPTIME = form.getvalue('maq2_uptime')

#ATRIBUTOS DA MAQUINA 3
cbxM3PS = form.getvalue('maq3_ps')
cbxM3DF = form.getvalue('maq3_df')
cbxM3FINGER = form.getvalue('maq3_finger')
cbxM3UPTIME = form.getvalue('maq3_uptime')


#Set default fix values
vers = 2
ihl = 160
tSv = 0
fl = 0
fgoff = 0
time = 1
srcAd = bytes(HOSTD.encode('utf-8'))
hCheck = 0    # IMPLEMENTAR
global dAdrss
global prot
global opt
global id
global tam


def pureAdd(x):
    c = "."
    for i in range(0,len(x)):
        if x[i] == c:
            x.replace(x[i],"")  #retira . 

def novoPacote(daemon, function, identification):

    global prot
    prot = function

    global id
    id = identification

    global totalLength
    global dAd

    if (function == 1):  # PS
        if (daemon == 1):
            dAd = P1
            msg = "aux"
            #msg = form.getvalue('maq1-ps')
        elif (daemon == 2):
            dAd = P2
            msg = form.getvalue('maq2-ps')
        elif (daemon == 3):
            dAd = P3
            msg = form.getvalue('maq3-ps')


    elif (function == 2):  # DF
        if (daemon == 1):
            dAd = P1
            msg = form.getvalue('maq1-df')
        elif (daemon == 2):
            dAd = P2
            msg = form.getvalue('maq2-df')
        elif (daemon == 3):
            dAd = P3
            msg = form.getvalue('maq3-df')

    elif (function == 3):  # FINGER
        if (daemon == 1):
            dAd = P1
            msg = form.getvalue('maq1-finger')
        elif (daemon == 2):
            dAd = P2
            msg = form.getvalue('maq2-finger')
        elif (daemon == 3):
            dAd = P3
            msg = form.getvalue('maq3-finger')

    elif (function == 4):  # UPTIME
        if (daemon == 1):
            dAd = P1
            msg = form.getvalue('maq1-uptime')
        elif (daemon == 2):
            dAd = P2
            msg = form.getvalue('maq2-uptime')
        elif (daemon == 3):
            dAd = P3
            msg = form.getvalue('maq3-uptime')

    global opt

    dest = bytes(dAd.encode('utf-8'))

    if (msg):
        opt = bytes(msg.encode('utf-8'))
    else:
        msg = '0'
        opt = bytes(msg.encode('utf-8'))

    tam = len(msg)  #implementar

    #MONTA PACOTES
    pacote = bytes
    pacote = (struct.pack('hhhhhhhhhh255p255p255p', vers, ihl, tSv, tam, id, fl, fgoff, time, prot, hCheck, srcAd, dest, opt))

    resultado = ''
    resposta = bytes

    if(daemon==1):
        daemon1.sendall(pacote)
        while 1: 
            data = daemon1.recv(787)
            if not data: break 
            resposta = struct.unpack('hhhhhhhhhh255p255ph255p', data)
            resultado = resultado + resposta[13].decode('utf-8')
        daemon1.close()

    elif(daemon==2):
        daemon2.sendall(pacote)
        while 1: 
            data = daemon2.recv(1024)
            if not data: break 
            resposta = struct.unpack('hhhhhhhhhh255p255ph255p', data)
            resultado = resultado + resposta[13].decode('utf-8')
        daemon2.close()

    elif(daemon==3):
        daemon3.sendall(pacote)
        while 1: 
            data = daemon3.recv(1024)
            if not data: break 
            resposta = struct.unpack('hhhhhhhhhh255p255ph255p', data)
            resultado = resultado + resposta[13].decode('utf-8')
        daemon3.close()

    print(resultado)

cbxM1PS = 1
#CHAMADA DE PROTOCOLOS PARA M1
if(cbxM1PS):
    print(' Opcao PS da M1 selecionada:\n')
    novoPacote(1,1,11)

if(cbxM1DF):
    print(' Opcao DF da M1 selecionada:\n')
    novoPacote(1,2,12)

if(cbxM1FINGER):
    print(' Opcao FINGER da M1 selecionada:\n')
    novoPacote(1,3,13)

if(cbxM1UPTIME):
    print(' Opcao UPTIME da M1 selecionada:\n')
    novoPacote(1,4,14)


#CHAMADA DE PROTOCOLOS PARA M2
if(cbxM2PS):
    print(' Opcao PS da M2 selecionada:\n')
    novoPacote(2,1,21)

if(cbxM2DF):
    print(' Opcao DF da M2 selecionada:\n')
    novoPacote(2,2,22)

if(cbxM2FINGER):
    print(' Opcao FINGER da M2 selecionada:\n')
    novoPacote(2,3,23)

if(cbxM2UPTIME):
    print(' Opcao UPTIME da M2 selecionada:\n')
    novoPacote(2,4,24)

#CHAMADA DE PROTOCOLOS PARA M3
if(cbxM3PS):
    print(' Opcao PS da M3 selecionada:\n')
    novoPacote(3,1,31)

if(cbxM3DF):
    print(' Opcao DF da M3 selecionada:\n')
    novoPacote(3,2,32)

if(cbxM3FINGER):
    print(' Opcao FINGER da M3 selecionada:\n')
    novoPacote(3,3,33)

if(cbxM3UPTIME):
    print(' Opcao UPTIME da M3 selecionada:\n')
    novoPacote(3,4,34)