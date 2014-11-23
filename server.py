#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line
            linea = line.split()
            metodo = linea[0]

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(sys.argv) != 4:
        sys.exit("Usage: python server.py IP port audio_file")
    
    IP = sys.argv[1]
    PUERTO = sys.argv[2]
    fichero = sys.argv[3]
    print "Listening..."
    serv = SocketServer.UDPServer(("", PUERTO), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
