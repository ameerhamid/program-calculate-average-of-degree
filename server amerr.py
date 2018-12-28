import socket
def cal(message):
    pa=[]
    pa=message.split()
    if len(pa)==3:return (int(pa[0])+int(pa[1])+int(pa[2]))/3
serverport=12800
BUFFER_SIZE=1024
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind(('',serverport))
print('The server is ready to receive port 12800')
while 1:
    message,clientaddress=serversocket.recvfrom(BUFFER_SIZE)
    message=message.decode('utf-8')
    response=str(cal(message))
    serversocket.sendto(response.encode('utf-8'),clientaddress)
    print(response)
serversocket.close()