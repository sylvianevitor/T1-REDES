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

#Cadastro dos daemons
HOSTD = '127.0.0.1'
P1 = 9001
P2 = 9002
P3 = 9003

daemon1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
daemon2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
daemon3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#daemon1.connect((HOSTD, P1))
#daemon2.connect((HOSTD, P2))
#daemon3.connect((HOSTD, P3))

print("Content-Type: text/html;charset=utf-8\r\n\r\n")
#print('<meta chatset=\"utf-8\">')

print("webserver.py")

#Cria instancia de FieldStorage
form = cgi.FieldStorage()

#Get data from fields
#ATRIBUTOS DA MAQUINA 1
#cbxM1PS = form.getvalue('maq1_ps')
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
version = 2
typeOfService = 0
flags = 0
fragmentOffset = 0
timeToLive = 1
sourceAdress = HOSTD
global protocol
global options
global identification


def novoPacote(function, daemon, id):

    global protocol
    protocol = function

    global identification
    identification = id

    if (function == 1):  # PS
        if (daemon == 1):
            destinationAddress = P1
            #msg = form.getvalue('maq1-ps')
            msg = "hello"
        elif (daemon == 2):
            destinationAddress = P2
            msg = form.getvalue('maq2-ps')
        elif (daemon == 3):
            destinationAddress = P3
            msg = form.getvalue('maq3-ps')

    elif (function == 2):  # DF
        if (daemon == 1):
            destinationAddress = P1
            msg = form.getvalue('maq1-df')
        elif (daemon == 2):
            destinationAddress = P2
            msg = form.getvalue('maq2-df')
        elif (daemon == 3):
            destinationAddress = P3
            msg = form.getvalue('maq3-df')

    elif (function == 3):  # FINGER
        if (daemon == 1):
            destinationAddress = P1
            msg = form.getvalue('maq1-finger')
        elif (daemon == 2):
            destinationAddress = P2
            msg = form.getvalue('maq2-finger')
        elif (daemon == 3):
            destinationAddress = P3
            msg = form.getvalue('maq3-finger')

    elif (function == 4):  # UPTIME
        if (daemon == 1):
            destinationAddress = P1
            msg = form.getvalue('maq1-uptime')
        elif (daemon == 2):
            destinationAddress = P2
            msg = form.getvalue('maq2-uptime')
        elif (daemon == 3):
            destinationAddress = P3
            msg = form.getvalue('maq3-uptime')

    global options
    options = bytes(msg.encode('utf-8'))


    #MONTE PACOTES






cbxM1PS = 1;

if(cbxM1PS):
    print(' Opcao PS da M1 selecionada: ')
    novoPacote(1,1,11)




