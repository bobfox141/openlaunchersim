#!/usr/bin/env python3

# this is the launcher. valid launcher states are off, standby, armed, launching

class Launcher():
    OFF = 0
    STANDBY = 1
    ARMED = 2
    LAUNCH = 3 
    
       
    def __init__(self):
        fsm = OFF
        launcher_type = fixed
        pods_loaded = 1 
        rounds = 4
        expended = 0
        directional = true
        
        
    def rounds(self):
        return rounds
    
    def state(self):
        return fsm
    
    
    # initialize currently turns the launcher from off to standby
    # checks the rounds available and then waits for a target
    def init(self):
        fsm = STANDBY
        
        
        