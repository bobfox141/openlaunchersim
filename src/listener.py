import socket
import errno
import time

class Listener:
    HOST = '127.0.0.1'           # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    connected = False
    LAUNCHFREQ = 5
    commands = [ "O","S", "C", "A", "L", "W", "D" ]   # off, standby, active, arm, launch
    done = False
    command = ""
    
    def getListenerRef(self):
        return self
    
    def recv(self):
        command = ""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            print(f"Server listening on {self.HOST}:{self.PORT}")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        self.command_recv = True
                        self.command = data.decode()
                        print(f"Received from client: {self.command}")
                        conn.sendall(b"Server received your message:" + data)
            s.close()
        return command
        
    def getLastCommand():
        self.command_recv = False
        return    
    
    def go(self):
        
        while not self.done:
            r = self.recv()
            if r in self.commands:
                if r == "S":
                    print(f"Transitioning launcher to standby.")
                elif r == "Q":
                    print(f"Quit has been ordered. Shutting down.")
                    exit()
                elif r == "D":
                    w = self.recv()                
                    self.weapon = w # get the next byte
                elif r == "L":
                    print("Launch command issued.")
                elif r == "A":
                    print("Arm command issued.")
                elif r == "C":
                    print("Transition to active.")
                elif r == "O":
                    print("Powering down to safe mode, minimal power required.")
                else:
                    print("Invalid command issued.")
            else: 
                print("Command ignored.") 
            time.sleep(1/self.LAUNCHFREQ)       

def main():
    print("Running controller.py in stand alone mode:")
    l = Listener()
    l.go()


if __name__ == "__main__":
    main()
