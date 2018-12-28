import socket
print('program averg of degree  ')
print('')
serverip='127.0.0.1'
serverport=12800
BUFFER_SIZE=1024
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
opp=['math','eng','arabic']
while 1:
   x=input("degree math :")
   y=input("degree english :")
   o=input('degree Arabic :')
   message=(o+' '+x+' '+y)
   client.sendto(message.encode('utf-8'),(serverip,serverport))
   response,address=client.recvfrom(BUFFER_SIZE)
   print (response)

client.close()