#!/usr/bin/env python3
# file: controller
# this takes the place of a launch command system
# 

import time
import queue


class Controller:
    
    QUIT = 0
    STANDBY = 1
    ARM = 2
    LAUNCH = 3
    OFF = 4
    TARGET = 5
    coords = [30000, 30000, 250]
    
    
    
    
    def __init__(self):
        pass
    
    def send(self, message):
        
        
        
    
    def go(self, hz):
        waits = 1/hz
        while not done:
            command = input("Enter command [Q,S,A,L,O,T]: ")
            command = command.strip()
            command = command[0].upper()
            if command == "Q":
                send(QUIT)
            elif command = "S":
                send(STANDBY)
            elif command = "A":
                send(ARM)
            elif command = "L":
                send(LAUNCH)
            elif command = "O":
                send(OFF)
            elif command = "T":
                send(TARGET)
                send(coords)
            time.sleep(waits)            
