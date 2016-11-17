import socket
import sys

HOST = ""
PORT = 8934

def main():
#Setup socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error.msg:
        print("Unable to create socket")
        sys.exit()
    print("Socket created.")

    #Bind to adress
    try:
        s.bind((HOST,PORT))
    except socket.error.msg:
        print("Bind failed. Closing...")
        sys.exit()
    print("Socket bound.")

    #Start listening
    s.listen(10)
    print("Socket Listening")

    #Accept connection
    conn, addr = s.accept()
    print("Connected to %s:%s"%(addr[0],addr[1]))

if __name__ == "__main__":
    main()
