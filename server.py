#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os.path


SERVER_IP = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
FILE = sys.argv[3]

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        client_address = self.client_address[0]
        client_port = self.client_address[1]

        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion")

        while 1:
            # Leyendo línea a línea lo que nos envía el cliente.
            line = self.rfile.read()
            if not line:
                break
            else:
                print "El cliente nos manda " + line
                # Si no hay más líneas salimos del bucle infinito

#===================== PROGRAMA PRINCIPAL ====================================
if __name__ == "__main__":
    if len(sys.argv) == 4:
        if not os.path.isfile(FILE):
            sys.exit("No existe el archivo")
    else: 
        print "Usage: python server.py IP port audio_file"
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", SERVER_PORT), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
