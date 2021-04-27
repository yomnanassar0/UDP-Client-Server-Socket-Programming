from socket import *
serverIP = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print("The server is ready to receive")

nums=[]


for i in range(0,100):
    msg, clientAddress = serverSocket.recvfrom(2048)
    nums.append(int(msg))

if nums[99] == 1:

    serverSocket.sendto(bytes(str(sum(nums)),"utf-8"), clientAddress)
    serverSocket.sendto(bytes(str(sum(nums)/100),"utf-8"), clientAddress)

elif nums[99] == 2:

    serverSocket.sendto(bytes(str(max(nums)), "utf-8"), clientAddress)
    serverSocket.sendto(bytes(str(min(nums)), "utf-8"), clientAddress)

elif nums[99] == 3:
    nums.reverse()
    for i in range(1, 100):
        serverSocket.sendto(bytes(str(nums[i]), "utf-8"), clientAddress)

elif nums[99] == 4:
    nums.sort()
    for i in range(1, 100):
        serverSocket.sendto(bytes(str(nums[i]), "utf-8"), clientAddress)
