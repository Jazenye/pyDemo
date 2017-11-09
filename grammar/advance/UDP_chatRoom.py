# -*- coding: utf-8 -*-
from socket import *
from time import *

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    bindData = ('', 9989)
    udpSocket.bind(bindData)

    msg = "You can send message from now!"
    udpSocket.sendto(msg.encode('utf-8'), ('192.168.1.101', 8080))

    while True:
        recvInfo = udpSocket.recvfrom(1024)

        # echo server
        udpSocket.sendto(recvInfo[0], recvInfo[1])
        tick = asctime(localtime(time()))
        content, destInfo = recvInfo
        print("----- ", tick, " -----")
        print(destInfo, " :", content.decode('gb2312'), "\n")

    udpSocket.close()

if __name__ == "__main__":
    main()
