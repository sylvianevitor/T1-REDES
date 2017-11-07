import cgitb
import cgi
import socket
import subprocess
import string
import struct
from struct import *
import io

#Cadastro dos daemons
HOST = '127.0.0.1'
P1 = 9001

daemon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
daemon.connect((HOST, P1))

form = cgi.FieldStorage()

#Get data from fields
#ATRIBUTOS DA MAQUINA 1
cbxM1PS = form.getvalue('maq1_ps')
cbxM1DF = form.getvalue('maq1_df')
cbxM1FINGER = form.getvalue('maq1_finger')
cbxM1UPTIME = form.getvalue('maq1_uptime')

txtM1PS = form.getvalue('maq1-ps')
txtM1DF = form.getvalue('maq1-df')
txtM1FINGER = form.getvalue('maq1-finger')
txtM1UPTIME = form.getvalue('maq1-uptime')

#ATRIBUTOS DA MAQUINA 2
cbxM2PS = form.getvalue('maq2_ps')
cbxM2DF = form.getvalue('maq2_df')
cbxM2FINGER = form.getvalue('maq2_finger')
cbxM2UPTIME = form.getvalue('maq2_uptime')

txtM2PS = form.getvalue('maq2-ps')
txtM2DF = form.getvalue('maq2-df')
txtM2FINGER = form.getvalue('maq2-finger')
txtM2UPTIME = form.getvalue('maq2-uptime')

#ATRIBUTOS DA MAQUINA 3
cbxM3PS = form.getvalue('maq3_ps')
cbxM3DF = form.getvalue('maq3_df')
cbxM3FINGER = form.getvalue('maq3_finger')
cbxM3UPTIME = form.getvalue('maq3_uptime')

txtM3PS = form.getvalue('maq3-ps')
txtM3DF = form.getvalue('maq3-df')
txtM3FINGER = form.getvalue('maq3-finger')
txtM3UPTIME = form.getvalue('maq3-uptime')


#TESTE
print("cbxM1PS: = ", cbxM1PS)
print("txtM1PS: = ", txtM1PS)