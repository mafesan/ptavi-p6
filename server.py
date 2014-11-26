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
        #self.wfile.write("Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line
            linea = line.split(" ")
            metodo = linea[0]
            if len(linea) != 3:
                self.wfile.write("SIP/2.0 400 Bad Request" + '\r\n')
            else:
                if metodo == 'INVITE':
                    self.wfile.write("SIP/2.0 100 Trying" + '\r\n')
                    self.wfile.write("SIP/2.0 180 Ringing" + '\r\n')
                    self.wfile.write("SIP/2.0 200 OK" + '\r\n')
                elif metodo == 'ACK':
                    print "ACK recibido..."
                    aEjecutar = './mp32rtp -i ' + sys.argv[1] + ' -p 23032 ' +\
                                '< ' + sys.argv[3]
                    print aEjecutar
                    print "Envio de RTP..."
                    os.system(aEjecutar)
                elif metodo == 'BYE':
                    print "BYE recibido..."
                    self.wfile.write("SIP/2.0 200 OK")
                elif metodo != 'INVITE' or 'ACK' or 'BYE':
                    self.wfile.write("SIP/2.0 405 Method Not Allowed" + '\r\n')
                # Si no hay más líneas salimos del bucle infinito
                if not line or "[""]":
                    break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(sys.argv) != 4:
        sys.exit("Usage: python server.py IP port audio_file")

    IP = sys.argv[1]
    PUERTO = int(sys.argv[2])
    archivo = sys.argv[3]
    try:
        fichero = open(archivo)
    except:
        print "Usage: python server.py IP port audio_file"

    print "Listening..."
    serv = SocketServer.UDPServer(("", PUERTO), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
