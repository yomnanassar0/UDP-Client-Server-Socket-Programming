import random
from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)




for i in range(0,99):
    num = random.randint(1,100)
    clientSocket.sendto(bytes(str(num),"utf-8"),(serverName, serverPort))

operator = random.randint(1,4)

clientSocket.sendto(bytes(str(operator),"utf-8"),(serverName, serverPort))


while i < 100:
    res = clientSocket.recv(2048)
    print(str(res))
clientSocket.close()