#!/usr/bin/env python3

# checks the command bus for a command, checks internal state for problems, waits.
# this is the launcher. valid launcher states are off, standby, armed, launching
# a launcher does a couple of things. interfaces to the weapon, powers the systems before the
# internal generator comes on line
# and fires the charge that lights the fuel sources.
# after that, it just returns to standby


import socket

class Launcher():
    OFF = 0
    STANDBY = 1
    ACTIVE = 2 
    ARMED = 3
    LAUNCH = 4 
    TARGET = 5
    WEAPSEL = 6
    
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
        self.mtype = t  # tgus us the weapon type. 
        self.expended = 0
        self.directional = true
        self.target = [0,0,0]   # target is x,y,z downrange in meters
        self.waypoint = [0,0,0] # a list of waypoints. first interation will not use this.
        
        self.done = False
        self.armed = False
        self.targetset = False
        self.buffer = ""
        

    def rounds(self):
        return self.rounds
    
    def state(self):
        return self.fsm
    
    # this is the main loop for the launcher
    def go(self):
        while not self.done:
            
            print("Current status: Launcher is ", end = "")
            if length(self.buf) > 0:
                command = self.buf[0]   # get the first char of buffer
                
            if self.fsm == self.OFF:
                print("OFF.")
                if command == self.STANDBY:
                    self.init() # transistion to standby
                    print("")
            elif self.fsm == self.STANDBY:
                print("STANDBY.")
                if command == self.ARMED:
                    self.armlauncher()
            elif self.fsm == self.ARM:
                
            elif self.fsm == self.LAUNCH:
            sleep(1000.0/5.0)        
                    
    def receiver(self):

        while not self.done:  
            self.buf = self.s.recv(1)  # receive data up to 128 bytes and put it in the buffer.  
            sleep(1000.0/5.0)    
            
    
    # initialize currently turns the launcher from off to standby
    # checks the rounds available and then waits for a target
    def init(self):
        self.fsm = self.STANDBY
        print("Powering the launcher to standby.")
        if self.selfcheck():
            print("Launcher: " + LID + "is available and accepting commands.")
        else
            print
        
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
        

    def getLauncherRef():
        return self

# the main only gets used when you call the module by filename as in 
# python launcher.py
if __name__ == "__main__":
    l = Launcher()
    l.go()