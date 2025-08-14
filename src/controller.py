#!/usr/bin/env python3
# file: controller
# this takes the place of a launch command system. It is effectively a client
# in the client server system. The server listens for commands. Once the weapon leaves the 
# launcher it is disconnected, and so it returns to active mode. Right now this is just a jumble 
# of code that doesn't actively do much. 

import time
import queue
import socket



class Controller:
    DEBUG = True
    LAUNCHFREQ = 5
    QUIT = 0
    OFF = 0
    STANDBY = 1
    ACTIVE = 3
    ARM = 4
    LAUNCH = 5
    coords = [30000, 30000, 250]
    commands = [ "O","S", "C", "A", "L" ]   # off, standby, active, arm, launch 
    HOST = '127.0.0.1'
    PORT = 65432
    

    def __init__(self):
        self.done = False

        # self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mode = "manual"
        # self.s.listen(5)
        # self.s.bind((self.HOST,self.PORT))
        # print("Bound socket on port: ", self.PORT)
        self.command = "O"
        
    def sendCommand(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(message.encode())   #encode the string into bytes and send it
            data = s.recv(128)           # receive the reflected packet
            print(f"Received from server: {data.decode()}")
            s.close()


    def close(self):
        self.s.close()

    # return the next command in the sequence for testing.
    def gencommand(self):
        comid = self.commands.index(self.command) + 1
        if comid > 4:
            comid = 0
        return self.commands[comid]

    def go(self, hz):
        waits = 1/hz     
        while not self.done:
            # if self.mode == "manual":
            command = input("Enter a command [ O, S, A, L, T, D, Q, ]: ")    # off, standby, arm, launch, target assigned, q
            # elif self.mode == "pattern":
            #    command = self.gencommand()
            #    if self.DEBUG:
            #        print("Command: %s"  % command)
            
            command = command.strip()
            command = command[0].upper()
            if command == "Q":
                print("Sending the Quit command.")
                self.sendCommand(command)
                self.done = True
            elif command == "S":
                print("Requesting transition to Standby Mode.")
                self.sendCommand(command)
            elif command == "A":
                print("Arm the default weapon.")
                self.sendCommand(command)
            elif command == "L":
                self.sendCommand(command)
            elif command == "O":
                self.sendCommand(command)
            elif command == "T":
                self.sendCommand(command)
                self.sendCommand(self.coords)
            elif command == "D":
                self.sendCommand(command)
                self.sendCommand("1")          # set the default weapon to 1
            time.sleep(waits)

    def main(self, hz):
        self.go(hz)



if __name__ == "__main__":
    print("Running controller.py in stand alone mode:")
    c = Controller()
    c.mode = "pattern"  #running 
    c.main(c.LAUNCHFREQ)
