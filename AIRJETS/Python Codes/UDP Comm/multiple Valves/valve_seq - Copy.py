import socket
import time 

 

#msgFromClient       = "1"



serverAddressPort   = ("192.168.0.2", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket
for i in range(1,63):
    msgFromClient = str(i)
    nextvalve= str(i+1)
    next_3rd_valve=str(i+2)
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    bytesToSend         = str.encode(nextvalve)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    bytesToSend         = str.encode(next_3rd_valve)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)


    time.sleep(.5)


    msgFromClient = "0"
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    time.sleep(1)



 

#msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

#msg = "Message from Server {}".format(msgFromServer[0])

#print(msg)