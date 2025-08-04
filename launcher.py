#!/usr/bin/env python3

# this is the launcher. valid launcher states are off, standby, armed, launching
# a launcher does a couple of things. interfaces to the weapon, powers the systems before the
# internal generator comes on line
# and fires the charge that lights the fuel sources.
# after that, it just returns to standby

import socket

class Launcher():
    OFF = 0
    STANDBY = 1
    ARMED = 2
    LAUNCH = 3 
    
    QUIT = 0
    LSTANDBY = 1
    ARM = 2
    TARGET = 5
    
    
    AIM9X = 0
    STING = 1
    TAMIR = 2
    HARMS = 3
    JAVEL = 4
    
    LAUNCHERFREQ = 5
    
    
    def __init__(self, r, t):
        self.fsm = OFF
        self.launcher_type = fixed
        self.pods_loaded = 1 
        self.rounds = r
        self.mtype = t
        self.expended = 0
        self.directional = true
        self.target = [0,0,0]   # target is x,y,z downrange in meters
        self.waypoint = [0,0,0] # a list of waypoints. first interation will not use this.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = 54000
        self.s.bind(('',self.port))
        self.s.listen(5)   # max 5 connections set up for the listen.
        self.done = False
        self.armed = False
        self.targetset = False
        self.buffer = ""
        
    def recv(self):
        self.buffer = self.s.recv(128)  # receive data up to 128 bytes and put it in the buffer.
        return self.buffer
        
        
        
    def rounds(self):
        return self.rounds
    
    def state(self):
        return self.fsm
    
    # this is the main loop for the launcher
    def go(self):
        
        while not self.done:
            buf = self.recv()  # check the socket for a command
            if length(buf) > 0:
                command = buf.decode()
            print("Current status: Launcher is ", end = "")
            if self.fsm == self.OFF:
                print("OFF.")
                if command == self.STANDBY:
                    self.init() # transistion to standby
                    print("")
            elif self.fsm == self.STANDBY:
                print("STANDBY.")
                if command == self.ARMED:
                    self.armlauncher()
                 
                    

    
    # initialize currently turns the launcher from off to standby
    # checks the rounds available and then waits for a target
    def init(self):
        self.fsm = self.STANDBY
        printf("Powering the launcher on.")
        
    def armlauncher(self):
        self.fsm = self.ARMED
        self.armed = True
        self.setTarget([])
        self.targetset = True
        
    def setTarget(self, t):
        self.target = t
        
    # so the launcher stays in launch mode till the missile exits. 
    def launch(self, t, w):
        self.fsm = self.LAUNCH
        # check to make sure we were armed 
        # and the target is set
        
        
    def poweroff(self):
        self.fsm = self.OFF
        
        


if __name__ == "__main__":
    l = Launcher()
    l.go()