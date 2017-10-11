#coding=utf-8
# 1. 获取指定文件夹中的所有文件名字， 并存放到变量中
# 2. 使用循环遍历的方式 对每个文件名进行修改
#    2.1 open
#    2.2 rename

import os

# 定义一个函数： 用来修改文件名， 并打印
def reName():
    os.rename(folderPath + filename, folderPath + newFileName)
    print(filename)

# folderPath ： 批处理文件名路径
# changeFlag : 批处理操作， add 新增前缀， del 删除所有前缀, new 添加默认文件, remove 移除该文件夹下所有文件
folderPath = "./temp/"
fileNameList = os.listdir(folderPath)
changeFlag = "remove"  # add or del or new or remove
prefix = '[author@jazen]-'

if not fileNameList: # 判断文件夹是否为空
    print("This file is EMPTY! ")
for filename in fileNameList:
    newFileName = filename
    if changeFlag == "add":
        newFileName = prefix + filename  # 给文件名加上前缀
        reName()
    elif changeFlag == "del":
        num = filename.rfind(prefix)
        if num >= 0:   # 检测前缀是否存在 prefix
            length = len(prefix)
            newFileName = filename[num+length: ]
        else:
            print("Cann't be simplify anymore")
        reName()
    elif changeFlag == "remove":
        os.remove(folderPath + filename)
    else:
        if changeFlag == "new":
            break
        print("changeFlag Error, please ensure its value in the list: [add, del, new, remove] !")

if changeFlag == "new":
    for i in range(3):
        f = open(folderPath + str(i+1) + ".txt", "w")
        f.write(" ")
        f.close()