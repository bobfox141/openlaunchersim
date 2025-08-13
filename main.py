#!/usr/bin/env python3
# file: main.exe
# desc: this is the main application launcher test scenario. It's just a loop proof of concept. 
# a launcher simulation works in stages, first stage, power up, wait for instructions we'll call this stand-by
# second stage, arm a missile (this generally means power is applied), load a target directive and 
# third stage, launch the missile --> after launch three choices, power-off (i.e. out of ordinance),
#   return to standby, arm and and launch second shot
# fourth stage, power down and lock the launcher

import threading
import sys

import controller

def main(argc, argv):
    
    threadcontroller = threading.Thread(target = Controller.go)        # default loop value. probably can go much slower
    threadcontoller.start()
    threadlistener = Thread(target = Listener.go)
    threadlistener.start()

    


if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv
    main(argc, argv)
