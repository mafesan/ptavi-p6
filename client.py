#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
IGNACIO ARRANZ AGUEDA - ISAM - PTAVI - PRACTICA 6
"""

import socket
import sys

# CAMPOS => METODO | DIRECCION SIP
if len(sys.argv) == 3:
	METODO = sys.argv[1]
	DIRECCION = sys.argv[2]
else:
	print "Usage: python client.py method receiver@IP:SIPport"

# Proceso de corte de la variable DIRECCION.
DIRECCION = DIRECCION.split("@")
NAME = DIRECCION[0]
DIRECCION = DIRECCION[1].split(":")
# IP y PUERTO del receptor
IP_SERVER = DIRECCION[0]
PORT = int(DIRECCION[1])

# Contenido que vamos a enviar
LINE = METODO + " sip:" + NAME + "@" + IP_SERVER + " SIP/2.0"
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP_SERVER, PORT))

try:
	print "Enviando: " + LINE
	my_socket.send(LINE + '\r\n')
	data = my_socket.recv(1024)
	print 'Recibido -- ', data
	# Cerramos todo
	my_socket.close()
	print "Fin."
except:
	print "Error: No server listening at", IP_SERVER, "port",PORT