#!/usr/bin/python
 
import os, sys
import SocketServer
import socket
import subprocess
from pyfirmata import Arduino, util
import time
#imports for PiBrainRelay
import time

PORT = '/dev/ttyS0' #REAL

# Creates a new board 
board = Arduino(PORT, baudrate=57600)
print "Connecting to Alamode"
LED = board.get_pin('d:13:o')


RELAY1 = 7
RELAY2 = 6
RELAY3 = 5
RELAY4 = 4



LED.write(1)
time.sleep(0.5)
LED.write(0)
time.sleep(0.5)
LED.write(1)
time.sleep(1)
LED.write(0)
time.sleep(0.75)
LED.write(1)
time.sleep(1)
LED.write(0)
time.sleep(0.75)
LED.write(1)
time.sleep(1)
LED.write(0)



print "Connected to Alamode" 

class Control():
    def relayAllOff():
        board.digital[RELAY1].write(0)
        board.digital[RELAY2].write(0)
        board.digital[RELAY3].write(0)
        board.digital[RELAY4].write(0)
       
    def relayAllOn():
        board.digital[RELAY1].write(1)
        board.digital[RELAY2].write(1)
        board.digital[RELAY3].write(1)
        board.digital[RELAY4].write(1)

    def relay1Off():
        board.digital[RELAY1].write(0)

    def relay1On():
        board.digital[RELAY1].write(1)
    
    def relay2Off():
        board.digital[RELAY2].write(0)
    
    def relay2On():
        board.digital[RELAY2].write(1)
    
    def relay3Off():
        board.digital[RELAY3].write(0)

    def relay3On():
        board.digital[RELAY3].write(1)

    def relay4Off():
        board.digital[RELAY4].write(0)
    
    def relay4On():
        board.digital[RELAY1].write(1)
    
  

class PiBrainServer(SocketServer.BaseRequestHandler):
    print "Serving"
    def handle(self):
        try:
 
            # self.request is the TCP socket connected to the client
            
            self.data = self.request.recv(1024).strip()
            print "{} wrote:".format(self.client_address[0])
            print self.data
            print "--------------------------------------------------"
            #act on the relay
            if self.data == "Allon":
                board.digital[RELAY1].write(1)
                board.digital[RELAY2].write(1)
                board.digital[RELAY3].write(1)
                board.digital[RELAY4].write(1)
                
            elif self.data == "ALLoff":
                board.digital[RELAY1].write(0)
                board.digital[RELAY2].write(0)
                board.digital[RELAY3].write(0)
                board.digital[RELAY4].write(0)
                
            elif self.data == "Relay1On":
                board.digital[RELAY1].write(1)
                board.digital[RELAY2].write(1)
                board.digital[RELAY3].write(1)
                board.digital[RELAY4].write(1)
                
            elif self.data == "Relay1Off":
                switch.relay1Off()

            elif self.data == "Relay2On":
                switch.relay2On()
                
            elif self.data == "Relay2Off":
                switch.relay2Off()

            elif self.data == "Relay3On":
                    switch.relay3On()
                
            elif self.data == "Relay3Off":
                switch.relay3Off()
                 
            elif self.data == "Relay4On":
                switch.relay4On()
                
            elif self.data == "Relay4Off":
                switch.relay4Off()
            else:
                 print "command not recognized..."
               
                
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())
            
       
        except KeyboardInterrupt:
            this.socket.close()
            board.close()
            print "Exiting"
            sys.exit()
        except IOError:
            print "IOError"
 
 
if __name__ == "__main__":

   
    print socket.gethostname()
    HOST, PORT = "", 33733
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), PiBrainServer)
 
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
 
