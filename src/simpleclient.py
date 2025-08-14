import socket

class SimpleClient():
    # attributes
    commands = [ "O","S", "C", "A", "L", "W", "D" ]   # off, standby, active, arm, launch 
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    count = 0
    
    def advanceCommand(self, c):
        self.count = self.count + 1
        if self.count > 4:
            self.count = 0
        
    
    
    def sendCommand(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(message.encode())   #encode the string into bytes and send it
            data = s.recv(1024)           # receive the reflected packet
            print(f"Received from server: {data.decode()}")
            s.close()

    def go(self):
         message = self.commands[self.count]
         self.sendCommand(message)
        

if __name__ == "__main__":
    print("Instantiating class")
    c = SimpleClient()
    print("Calling routine go()")
    c.go()
