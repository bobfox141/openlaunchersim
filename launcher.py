#!/usr/bin/env python3

# this is the launcher. valid launcher states are off, standby, armed, launching
# a launcher does a couple of things. interfaces to the weapon, powers the systems before the
# internal generator comes on line
# and fires the charge that lights the fuel sources.
# after that, it just returns to standby

class Launcher():
    OFF = 0
    STANDBY = 1
    ARMED = 2
    LAUNCH = 3 
    
    AIM9X = 0
    STING = 1
    TAMIR = 2
    HARMS = 3
    JAVEL = 4
       
    def __init__(self, r, t):
        fsm = OFF
        launcher_type = fixed
        pods_loaded = 1 
        rounds = r
        mtype = t
        expended = 0
        directional = true
        target = [0,0,0]   # target is x,y,z downrange in meters
        waypoint = [0,0,0] # a list of waypoints. first interation will not use this.
        done = false
        
        
        
    def rounds(self):
        return self.rounds
    
    def state(self):
        return self.fsm
    
    # this is the main loop for the launcher
    def go(self):
        if self.fsm == OFF:
            if DEBUG == true:
                print("Launcher is off, waiting...")
            sleep(1) # if the launcher is off, wait
        else 
            while (self.done == true):
            
    
    # initialize currently turns the launcher from off to standby
    # checks the rounds available and then waits for a target
    def init(self):
        fsm = STANDBY
        
    def armlauncher(self):
        fsm = ARMED
        
    def setTarget(self, t):
        self.target = t
        
        
        
        
