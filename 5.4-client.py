import socket
import sys

if(len(sys.argv) >1):
   ServerIP = sys.argv[1]
else:
   exit(1)

s = socket.socket()
PORT = 9898
s.connect((ServerIP, PORT))

print("\n Which file you want to sent?")
filename = input("\n Enter filename : ")
print(" Filename : " + filename)


file = open(filename, "rb")
SendData = file.read(1024)

while SendData:
    print("\n\n -----Below message is received from server----- \n\n", s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)


s.close()
