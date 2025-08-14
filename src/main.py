#!/usr/bin/env python3
# main.py
# runner for the client server test

import threading
import controller
import listener

def main():
    print("Running main caller for the two programs.")
    c = controller.Controller()
    c.mode = "pattern"
    hz = 5 
    l = listener.Listener()
    # i think the listener has to go first.
    print("Starting listener thread")
    tl = threading.Thread(target = l.go(hz))  
    tl.start()
    print("Starting controller thread")
    tc = threading.Thread(target = c.go(hz))
    tc.start()
    
if __name__ == "__main__":
    main()
