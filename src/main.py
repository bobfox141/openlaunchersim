#!/usr/bin/env python3
# main.py
# runner for the client server test

import threading
import controller
import listener

def main():
    print("Running main caller for the two programs.")  # the controller is the client it mimics IBCS
    print("Starting listener thread")   # the listener is the server
    l = listener.Listener()
    tl = threading.Thread(target = l.go())  
    tl.start()
    
    c = controller.Controller()
    c.mode = "pattern"
    hz = 5
    print("Starting controller thread")
    tc = threading.Thread(target = c.go())
    tc.start()
    
    ln = launcher.Launcher()
    print("Starting launcher.")
    print("Starting the launcher thread.")
    tln = threading.Thread(target = ln.go())
    tln.start()    
    
if __name__ == "__main__":
    main()
