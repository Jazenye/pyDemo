# -*- coding: utf-8 -*-
from socket import *
import struct
import os

localIP = "127.0.0.1"
serverPath = "E:\Tftpd32\server"

def main():
    # print list of filename
    catalog = os.listdir(serverPath)
    for i in catalog:
        print(i) 

    # filename = "test.jpg"
    filename = input("\n请输入文件名称:")
    f = open(filename, "wb")
    
    # read/write request: 1 read, 2 write
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    rwRequest = struct.pack("!H%dsb5sb" % len(filename), 1, filename.encode("utf-8"), 0, "octet".encode("utf-8"), 0)
    udpSocket.sendto(rwRequest, (localIP, 69))

    docNum = 0
    couldDownload = True
    while True:
        resData = udpSocket.recvfrom(1024)
        recvData, serverInfo = resData

        # 从返回的数据中获取 操作码 和 块编码
        optionCode = struct.unpack("!H", recvData[:2])[0]  # return tuple
        blockCode = struct.unpack("!H", recvData[2:4])[0]

        # 校对块编码
        if optionCode == 3:
            docNum += 1
            if docNum == 65536:
                docNum = 0

            # 写入文件
            if docNum == blockCode:
                f.write(recvData[4:]) 

            # 发送ACK
            ACKcode = struct.pack("!HH", 4, blockCode)
            udpSocket.sendto(ACKcode, serverInfo)

        # 错误信息处理
        elif optionCode == 5:
            couldDownload = False  
            print("Error!", blockCode) 
            print("error code:", blockCode, "\nerror message: ", recvData[4:-1].encode("utf-8"))

        # 结束传输
        if len(recvData) < 516: 
            break
        
    # 如果没有要下载的文件，就删除刚下载的文件
    if couldDownload:
        f.close()
    else:
        try:
            os.unlink(filename)  
        except (PermissionError, IOError):
            print("*** input error ***")
        finally:
            print("--- operate done ---")

    udpSocket.close()


if __name__ == "__main__":
    operation = 1
    while operation != 0:
        print("0. quit,\n1. download,\n2. upload\n")
        print("Please input a number to decide download or upload a file:")
        operation = int(input(""))

        if operation == 1 or operation == 2:
            main()
            # main(operation)
        elif operation != 0:
            print("Please input agagin!")
    print("quit success!")
