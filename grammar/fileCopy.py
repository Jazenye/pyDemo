#coding=utf-8

# 1. 用户输入文件名
# 2. 打开文件并读取文件中的数据,
# ps: read() & readlines() 会一次性读取文件内容 可能会导致内存空间不够 故使用readline()或read(num) + loop实现
# 3. 读取文件数据
# 4. 组织一个新的文件名字
# 5. 新建一个文件, 并写入 ( loop )

oldFileName = input("请输入需要拷贝的文件名称： ") # fileCopy.txt

# create new file name
num = oldFileName.rfind(".")
lName = oldFileName[0:num]
rName = oldFileName[num:]
newFileName = lName + "[复件]" + rName

# read content of old file
oldFile = open(oldFileName, "r")
newFile = open(newFileName, "w")

# get & copy content from old file to new file
content = oldFile.readline()
while len(content) > 0:
    newFile.write(content)
    content = oldFile.readline()

# close file flow
oldFile.close()
newFile.close()