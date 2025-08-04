#!/usr/bin/env python3
# file: controller
# this takes the place of a launch command system. It is effectively a client
# in the client server system. The server listens for commands 

import time
import queue
import socket

class Controller:
    LAUNCHFREQ = 5
    QUIT = 0
    STANDBY = 1
    ARM = 2
    LAUNCH = 3
    OFF = 4
    TARGET = 5
    coords = [30000, 30000, 250]
    
    
    
    
    def __init__(self):
        self.done = False
        self.host = '127.0.0.1'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.port = 54000
        self.s.bind(('',self.port))
        print("Bound socket on port: ", self.port)
        
    
    def send(self, message):
        # this will fail if the receiving connection isn't open
        # with 'broken pipe'
        self.s.send(message.to_bytes()) 
        
    def close(self):
        self.s.close()
        
    
    def go(self, hz):
        waits = 1/hz
        while not self.done:
            command = input("Enter a command [Q,S,A,L,O,T]: ")
            command = command.strip()
            command = command[0].upper()
            if command == "Q":
                self.send(self.QUIT)
                self.done = True
            elif command == "S":
                self.send(self.STANDBY)
            elif command == "A":
                self.send(self.ARM)
            elif command == "L":
                self.send(self.LAUNCH)
            elif command == "O":
                self.send(self.OFF)
            elif command == "T":
                self.send(self.TARGET)
                self.send(self.coords)
            time.sleep(waits)            
    
    def main(self, hz):
        self.go(hz)



if __name__ == "__main__":
    print("Running controller.py in stand alone mode:")
    c = Controller()
    c.main(c.LAUNCHFREQ)