#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os


if len(sys.argv) == 4:
    SERVER_IP = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])
    FILE = sys.argv[3]
    if not os.path.isfile(FILE):
        sys.exit("Usage: python server.py IP port audio_file")
else:
    sys.exit("Usage: python server.py IP port audio_file")

class EchoHandler(SocketServer.DatagramRequestHandler):


    def handle(self):
        """
        Server SIP
        """
        print "Listening..."

        client_address = self.client_address[0]
        client_port = int(self.client_address[1])

        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion\r\n\r\n")

        while 1:
            # Leyendo línea a línea lo que nos envía el cliente.
            line = self.rfile.read()
            if not line:
                break
            else:
                print "Mensaje de entrada " + line
                line = line.split()
                line[1] = line[1].split(":")
                if line[0] == "INVITE" and line[2] == "SIP/2.0":
                    self.wfile.write("SIP/2.0 100 Trying\r\n\r\n" 
                                        + "SIP/2.0 180 Ring\r\n\r\n" 
                                        + "SIP/2.0 200 OK\r\n\r\n")
                elif line[0] == "ACK":
                    print "Comienza la transmision........."
                    Streaming = './mp32rtp -i 127.0.0.1 -p 23032 < ' + FILE
                    os.system(Streaming)
                    print "Fin de la emision"
#===================== PROGRAMA PRINCIPAL ====================================
if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", SERVER_PORT), EchoHandler)
    serv.serve_forever()