import socket

s = socket.socket()

port = 9898
print("\n Server is listening on port :", port,"\n")

s.bind(('', port))

s.listen(10)

file = open("file.txt", "wb")
print(" File.txt will be copied at server side.")
print("******************************************")

while True:
    conn, addr = s.accept()


    msg ="\n -------------------------------------\n Hi Client[IP address: "+ addr[0] + "] \n **Welcome to Server**\n -------------------------------------\n\n"
    conn.send(msg.encode())

    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)

    file.close()
    print("\n File has been coppied successfully.")

    conn.close()
    print("\n Server closed the connection.\n")

    
    break
