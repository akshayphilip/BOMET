import socket
import time 

 

#msgFromClient       = "1"



serverAddressPort   = ("192.168.0.2", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket
for i in range(1,6):
    msgFromClient = str(i)
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    time.sleep(1)


    msgFromClient = "0"
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    time.sleep(1)



 

#msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

#msg = "Message from Server {}".format(msgFromServer[0])

#print(msg)