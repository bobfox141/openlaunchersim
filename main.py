#!/usr/bin/env python3
# a launcher simulation works in stages 
# first stage, power up, wait for instructions we'll call this stand-by
# second stage, arm a missile (this generally means power is applied), load a target directive and 
# third stage, launch the missile --> after launch three choices, power-off (i.e. out of ordinance),
#   return to standby, arm and and launch second shot
# fourth stage, power down and lock the launcher




from launcher import Launcher
from missile import Missile
from utility import * as ut
from pynput import keyboard as kbd
from time import *

LOOPTIME = 200 # 5 hz. 1000/5, right?

ESC = 27

def on_press(key):
    if key == keyboard.Key.esc:
        return ESC

# /I should probably just call this the main loop

def simlaunch():
    done = false   
    wait = false
    u = ut.Utility
    
    
    
    while not done:
        ## this starts the sim loop. lets just make it 5hz for laughs. 
        ## check to end the sim by keyboard
        ### Code that will read message bytes from a port

        now = time.perf_counter()
        elapsed_time = now - t0
        target_time = time_counter + CYCLETIME
        if elapsed_time < target_time:
            time.sleep(target_time - elapsed_time)

        # In the full program we write to a csv but in this simple program we will just print it
        milliseconds_since_epoch = datetime.datetime.now(timezone.utc)
        u.printf("Milliseconds since epoch: %f\n",milliseconds_since_epoch)

        time_counter += CYCLETIME
        ### Code that will read message bytes from a port

        now = time.perf_counter()
        elapsed_time = now - t0
        target_time = time_counter + CYCLETIME
        if elapsed_time < target_time:
            time.sleep(target_time - elapsed_time)

        # In the full program we write to a csv but in this simple program we will just print it
        milliseconds_since_epoch = datetime.datetime.now(timezone.utc)
        print(milliseconds_since_epoch)

        time_counter += CYCLETIME
        ### Code that will read message bytes from a port

        now = time.perf_counter()
        elapsed_time = now - t0
        target_time = time_counter + CYCLETIME
        if elapsed_time < target_time:
            time.sleep(target_time - elapsed_time)

        # In the full program we write to a csv but in this simple program we will just print it
        milliseconds_since_epoch = datetime.datetime.now(timezone.utc)
        print(milliseconds_since_epoch)

        time_counter += CYCLETIME
        ### Code that will read message bytes from a port

        now = time.perf_counter()
        elapsed_time = now - t0
        target_time = time_counter + CYCLETIME
        if elapsed_time < target_time:
            time.sleep(target_time - elapsed_time)

        # In the full program we write to a csv but in this simple program we will just print it
        milliseconds_since_epoch = datetime.datetime.now(timezone.utc)
        print(milliseconds_since_epoch)

        time_counter += CYCLETIME
                
def simreport():
    pass

def main():
    u = ut.Utility()
    listener = kbd.Listener(on_press=on_press)
    u.printf("Beginning a launcher simulation run:\n")
    simlaunch()
    u.printf("Ending a simulation run. Printing report.\n")
    simreport()
    






if __name__ == "__main__":
    main()