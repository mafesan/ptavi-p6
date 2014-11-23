#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.

# Dirección IP del servidor.
metodo = sys.argv[1]
datosreceptor = sys.argv[2]
listareceptor = datosreceptor.split('@')
receptor = listareceptor[0]
datosred = listareceptor[1]
datosred = datosred.split(':')
SERVER = datosred[0]
PORT = datosred[1]

if len(sys.argv) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")



# Contenido que vamos a enviar
LINE = metodo + 'sip:' + receptor + '@' + SERVER + 'SIP/2.0' 

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')
try:
    data = my_socket.recv(1024)
    print 'Recibido -- ', data
except socket.error:
    sys.exit("Error: No server listening at " + SERVER + "port " + PORT)

# respuesta al servidor
if metodo == 'INVITE':
    my_socket.send('ACK' + 'sip:' + receptor + '@' + SERVER + 'SIP/2.0')
if metodo == 'BYE':
    print "Terminando socket..."
    # Cerramos todo
    my_socket.close()
    print "Fin."
