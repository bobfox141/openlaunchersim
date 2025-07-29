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

from launcher import Launcher
from controller import Controller as ct



def main(argc, argv):
    
    thread = Thread(target = ct.go, args(5,) # default loop value. probably can go much slower
    thread.start()
	l = Launcher(4,1)
	l.go()


if __name__ == "__main__":
	argc = len(sys.argv)
	argv = sys.argv
	main(argc, argv)
