# -*- coding: utf-8 -*-
from threading import Thread
from socket import *

def msgSend(ip, port):
    destAddr = (ip, port)
    if destAddr:
        print("init Success, you could send message now!")
    else:
        print('Error')
        return 
    
    while True:
        message = input("<<< ")
        udpSocket.sendto(message.encode('gb2312'), destAddr)


def msgReceive():
    while True:
        recvMsg = udpSocket.recvfrom(1024)
        # print(recvMsg) :　(b'ok', ('192.168.1.101', 9999))
        print("\r>>> From ", recvMsg[1], ": ",recvMsg[0].decode('gb2312'))
        print("<<< ")
    

# 也可以将ip & port 设置为全局变量, 这样就不需要传递参数
udpSocket = None

def main():
    # 确认全局变量, 并创建套接字， 绑定端口
    global udpSocket 
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 7777))  # 这里数据必须是元组

    destIP = "192.168.1.101"
    destPort = 9999
    # destPort = int(input("输入对方的端口号："))

    thread_send = Thread(target=msgSend, args=(destIP, destPort))
    thread_receive = Thread(target=msgReceive)

    thread_send.start()
    thread_receive.start()

    thread_receive.join()
    thread_send.join()

    udpSocket.close()


if __name__ == "__main__":
    main()
