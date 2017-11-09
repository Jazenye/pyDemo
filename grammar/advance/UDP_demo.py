# -*- coding: utf-8 -*-
from socket import *

# UDP协议,  create socket
udpSocket = socket(AF_INET, SOCK_DGRAM)

# ip & port: ip⼀般不⽤写，表示本机的任何⼀个ip，三个IP的信息都接收, 绑定别人的ip 会崩溃
# 这里使用一个元组, 传入信息
bindData = ('', 9999)
udpSocket.bind(bindData)


sendData = input("请输入要发送的数据：")

destIP = "192.168.1.101"
destPort = 8080

# 指定发送信息， IP, port 
# udpSocket.sendto(b"msg", ("192.168.1.101", 8080))
udpSocket.sendto(sendData.encode("utf-8"), (destIP, destPort))

# receive message
recMsg = udpSocket.recvfrom(1024)

print("wait to receive message ...\n")
# print(recMsg)

content, destInfo = recMsg

print("Message: ",content.decode("gb2312") )
print("-- From ", destInfo)

print("\n---End---")

# close socket, otherwise port will be occupied
udpSocket.close()