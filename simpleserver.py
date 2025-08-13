import socket



class SimpleServer():   
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    weapon = "U"        # unselected.
    done = False
    
    
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
                    command = data.decode()
                    print(f"Received from client: {command}")
                    conn.sendall(b"Server received your message:" + data)
            s.close()
        return command
        
        
    
    def go(self):
        
        while not self.done:
            r = self.recv()
            if r == "S":
                print(f"Transitioning launcher to standby.")
            if r == "Q":
                print(f"Quit has been ordered. Shutting down.")
                exit()
            if r == "D":
                w = self.recv()                
                self.weapon = w # get the next byte
                
                

if __name__ == "__main__":
    print("Instantiating class")
    s = SimpleServer()
    print("Calling routine go()")
    s.go()

            
        
