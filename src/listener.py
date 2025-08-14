import socket
import errno
import time

class Listener:
    HOST = '127.0.0.1'           # Standard loopback interface address (localhost)
    PORT = 54000        # Port to listen on (non-privileged ports are > 1023)
    connected = False
    LAUNCHFREQ = 5
    def go(self, hz):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.HOST, self.PORT))
        s.setblocking(False) 
        s.listen(5)
        print("waiting for connection")
        while not self.connected:
            try:
                conn, addr = s.accept()  # set to non blocking
                conn.setblocking(False)
                # guessing if we get here the connection was accepted. 
                self.connected = True
            except BlockingIOError as e:
                if e.errno == errno.EAGAIN or e.errno == errno.EWOULDBLOCK:
                    print(".", end = "")
                    time.sleep(.2)
                    pass
                else:
                    print(f"Error accepting connection {e}")
                    break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break
                
        print("got connection from", addr)
        while True:
            try:
                data = conn.recv(128)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                conn.sendall(data) # Echo back the received data
                sleep(1.0/hz)
            finally:
                s.close()


def main():
    print("Running controller.py in stand alone mode:")
    l = Listener()
    l.go(l.LAUNCHFREQ)


if __name__ == "__main__":
    main()
