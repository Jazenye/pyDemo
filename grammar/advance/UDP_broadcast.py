# -*- coding: utf-8 -*-
from socket import *
import os

udpSocket = socket(AF_INET, SOCK_DGRAM)
dest =  ('<broadcast>', 7788)

udpSocket.sendto(b'Hi, Nice to meet you', ('192.168.1.101', 9999))
print("You coud receive message now")

while True:
    (message, addr) = udpSocket.recvfrom(1024)
    # print(meesage, addr)
    print("message: ", message)
    print("  -- from:", addr)
                           
udpSocket.close()