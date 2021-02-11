import threading 
import socket


HEADER=64#used to get data from the clients
#typical most used port
Port=5050
Server=socket.gethostbyname(socket.gethostname())
address = (Server, Port)
DISCONNECT_MSG="Disconnect"
#this is how to make a socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)##THIS ONE STANDS FOR IPV4,this other one just a network protocol that means we are streaming data through the socket
server.bind(address)##now we just bind the socket with the address now that means that each time we connect to this address it will tap into the above socket
#the soul purpose of this function is to handle connections between the individual clients and the server each connection will be runing on a seperate thread
def handleIndividualClientsConnections(sockets, address):
    print(f"[New Connection] {address} is Connected.")
    while True:
        msgLenght=socket.recv(HEADER).decode('utf-8')
        msgLenght=int(msgLenght)
        msg=sockets.recv(msgLenght).decode('utf-8')
        print(f"[{address}] {msg}")
        #we need to check at each time if the client wanted to disconnect
        if(msg == DISCONNECT_MSG):
            break;
        print(f"[{address}] {msg}")
    sockets.close() #disconnect

def disturbuteConnections():
    server.listen()#we set it to listen to comming connections
    print(f"[Listening] on {Server}")
    while True:#Just basicly saying we wanna keep listening
        Socket, address =server.accept()#What port and ip address is connected to the server going to be returned to address
        thread=threading.Thread(target=handleIndividualClientsConnections,args=(socket,address))
        thread.start()
        print(f"[Current Connections] {threading.activeCount() -1 }")#the minus one is just to not count the distrubte connection one the server launches
print("The Server is Launching in 1...2...3....  .....xD:")
disturbuteConnections();