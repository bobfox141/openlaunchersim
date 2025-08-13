#!/usr/bin/env python3
# file: listener.py
# descriptions: this just listens to the port at puts the commands on the queue

import time
import socket
import threading

class Listener:
    
    HOST = ''
    port = 54000
    
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.port))
        self.s.listen(5)
   
    def stoplisten(self):
        self.done = true
        
    def lastcommand(self):
        return self.buf
    
    def listen(self):
        cl, addr = self.s.accept()
        while not self.done:
            # accept the connection
           
            print("Connection requested from %s" % str(addr))
            tnow = time.ctime(time.time()) + "\r\n"
            self.buf = recv(1) # get a command
            if self.buf > 0:
                print("Command: %c" % self.buf)
            sleep(.5)
            
def main():
    c = Listener()
    t = threading.Thread(target = c.listen)
    t.start()
    
    
            
# if called to test run it this way            
if __name__ == "__main__":
    main()
