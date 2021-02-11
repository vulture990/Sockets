import socket 

HEADER=64#used to get data from the clients
#typical most used port
Port=5050
Server=socket.gethostbyname(socket.gethostname())
address = (Server, Port)
DISCONNECT_MSG="Disconnect"
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

def sendMsg(msg):
    message=msg.encode('utf-8')#encode the string into bytes to sent it as socket
    msgLen=len(message)
    sendLen=str(msgLen).encode('utf-8')
    sendLen+=b' ' * (HEADER - len(sendLen))
    client.send(sendLen)
    client.send(message)

sendMsg("Im CLIENT")