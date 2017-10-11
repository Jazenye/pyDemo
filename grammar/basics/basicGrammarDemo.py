#coding=utf-8

'''
  单引号 多行注释
'''

import random
import time
import os

age = int(input("Input your age : ")) # default type is str,  using int() transform type of data
print(type(age))  # <class 'int'>
if age >= 18:
    print("澳门最大赌场开业啦!")
elif not (age > 0 and age < 100) :
    print("Error!")
elif age < 17 or age == 17:
    print("Hey boy !")
else:
    pass

i = 0
while i < 3:
    print("random number: ",random.randint(0, 2)) # return a random number between 0 and 2
    # print(random.randrange(0, 51, 2)) # 0-50, +=2
    # print("i = %d"%i) # %d Symbol decimal integer, %f float, %s string
    i += 1 # there is no self add operator in python

def separator(name):
    print("-" * 25)  # define a function to print separator
    print("I'm the separator of : "+name)
    print("*" * 20)

sum = 0
for j in range(101): # create j between 0 and 100,  auto run j += 1
    if( j == 50):
        continue # break and continue only used in loop
    elif j == 101:
        print(sum)
        break  # never run this statement
    sum += j
print("sum = ", sum) # 5000


separator("loop")
# loop: for and while
str = "jazen"
j = 0
while j < 5:
    print("%s "%str[j], end='')  # in order to prevent line feed
    j += 1
# for key in name: print(key)
print(str[0:4], str[1:])  # jaze  azen ;  str[a:b] -> [a,b)


separator("string")
# some method of str
strDemo = "Welcome to Python World , let's start together!"
print(strDemo.find("come"), strDemo.rfind("to"))  # start index, if not find return -1
print(strDemo.find("password", 0, len(strDemo)))  # search range in [0, 47)  ; len(strDemo) => 47, string length,
print(strDemo.count("a"))  # return the total number of strDemo whose char=="a"
print(strDemo.startswith("Welcome"))  # return boolean
print(strDemo.lower(), strDemo.upper())  # lower case & capital

newStrDemo = strDemo.replace("to", "TOOOO")  # replace special str and return new string
print(newStrDemo, strDemo)

strArr = strDemo.split(" ", 2)  # divided str into three sections with  " "
print(strArr)
print(strDemo.split(" "))  # second arg could be omit
print(" + ".join(strArr))  # the function of String, joint array with String to a newString

separator("string method")

shortStr = "String"
print(shortStr.rjust(10), "+", shortStr.ljust(10), ";")  # supplement with whitespace into length  (formatting)
longStr = shortStr.center(20)
print("\'", longStr, "\'")
print("\'", longStr.rstrip(), "\'")  # delete some whitespace in the specified direction, likely lstript()
print(longStr.partition("i"))  # likely lpartition(), splite the string into three part separated by "i"

'''
    isdigit, isalpha 判断字符串是否均为字母， 数字 return boolean
    isalnum 判断所有字符都是字母或数字则返回 True,否则返回 False
    isspace, isupper 是否只包含空格、大写
'''


separator("List")
# some operation of list
pyList = ["String", "name", 1.1, 500]  # list could contain different types of data
temp = 0
while temp < len(pyList):  # let length = len(pyList) is better , save time to calculate
    print("pyList[%d] = %s "%(temp, pyList[temp])) # pyList[0] = String ...
    temp += 1

movieList = ["泰坦尼克", "星际穿越", "记忆碎片"]
for j in movieList:  # j = key
    print("%s  " % j, end='')

# add a new movie to movieList and print them
newMovie = input("\n请输入想要增加的电影名字： ")
movieList.append(newMovie)
print("new movie list : ")
for j in movieList:
    print("%s  " % j, end='')

# delete method： del list[i],  list.remove(name), list.pop()
while True:
    index, movie = input("\n输入要删除的电影序号,以及一个不同的电影名称: ").strip().split()  # 用空格分割多个输入

    if int(index) > len(movieList):
        print("Index bound! Please input again!")
    elif movie in movieList:  # 检查电影是否在电影列表中, 如果在电影列表中则删除该电影
        movieList.remove(movie)
        del movieList[int(index)]  # 删除序号对应的电影
        print(" delete success ! ")  #  exit loop after delete success
        break
    else:
        print("movie or index is not exits! Please input again!")

for j in movieList:
     print("%s  " % j, end='')


separator("dictionaries")
# 字典的存储形式 key: value
dic = {"name": "jazen", "language": "python"}
if "C++" in dic.values():
    print("C++ in dic")
elif ("name" in dic) and (dic.__contains__('name')):  # 检查 键 是否在 字典 中, if python2  dict.has_key()
    print("dic[name]: ", dic["name"])  # jazen
else:
    print("none")

dic["info"] = "new something"  # append new element
del dic["name"]
dic.pop("language")  # pop(key) ,  dic.clear() -> clear dictionary
print(dic, ", lenth: ", len(dic), ", keys: ", dic.keys() )  # len(dictionary) return the number of keys

# 遍历字典的key-value
newDic = {"name": "Zhangsan", "sex": "male", "age": 22}
print(newDic.items()) # print all items,返回字典的key value 值
for key, value in newDic.items():
    print("key = %s, value = %s " % (key, value))

# mix in list & dictionary
listDic = ["key0", 100]
listDic.append(newDic)
print(listDic[2]["name"])  # get value of the newDic in the listDic


separator("tuple")
# 元组()， 数组[], 字典{}
# tuple(), unable to change
tuple = ("zhangsan", 100)
tup1 = (1, 2, 3)
tup2 = (4, 5)
print(tup1 + tup2)  # element in the tuple cann't be changed
print(tuple * 3, tuple[0:], tuple[-1])
print(max(tup1), min(tup2))  # max(tup1) -> 3, min(tup2) -> 4


separator("function")
# 默认参数与可变参数, *args 结果类型是元祖，传递值是任意类型
# **kwargs结果类型是字典，传递值是以 key = value 方式传入
def calc(sum = 0, *numbers):
    for n in numbers:
        sum = sum + n
    return sum

print(calc(0, 1, 2, 3))  # 6

def test():
    global PAI  # 声明全局变量最好用大写， 且声明时无法初始化. ERROR: global PAI = 3.14
    PAI = 3.14

test()  # 如果不执行该函数,则全局变量无法被声明
print(PAI)  # could get the global variable out of function scope

def fib(n):  # 递归函数示例 斐波那契数列
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(2))

# 匿名函数，参数仅用逗号隔开，内容写在同一行，不需要return
lam = lambda a,b: a+b   # == (lambda a,b:a+b)(1,2)
print(lam(1,2))


separator("FILE")
# import os

# f = open("123.txt", "w")
# f.write("hello world")
# 前面参数为文件名，后面的为打开模式: r read, w write(有则覆盖，无则创建), a append
# a+, w+, r+ 都可读写, w+(有则覆盖，无则创建)
f = open("123.txt", "r+")
content = f.read(10)  # 如果不带参数，则一次性读取所有值， 文件指针+10
# type(content)  -> str
while len(content) > 0:
    print(content, end="***")
    # f.seek() 改变文件指针读写的位置,参数1：偏移量 可正可负; 参数2： 0 表示文件的开头， 1 表示当前位置，2表示文件末尾
    print("\n 文件指针当前位置： ", f.tell())
    content = f.read(10)  # 读取的位置会保存， 下一次读取从上次保存的地方开始读取
f.close()

# readline() & readlines()
# content = f.readline()
# while len(content):
#   content = f.readline()
#   print(content)

newFile = open("demo.txt", "r+")
# newFile.write("1Hello World! \n2Hello World! \n3Hello World! \n4Hello World! \n")
newContent = newFile.readlines()  # type(newContent)  -> list, 读取每一行存入
for temp in newContent:
    print(temp, end="")
newFile.close()


separator("exception")
# exception handling

try:
    print(num)  # NameError
    open("xxxx.txt", "r")  # IOError
# catch error
# python2 except (NameError, IOError), errMsg: errMsg是自定义的输出错误信息的变量
except (NameError, IOError) as errMsg:  # NameError 是错误类型，错误类型不匹配则无法捕获
    print(errMsg)
else:  # 这个子句将在try子句没有发生任何异常的时候执行
    print("Run success!")
finally:  # 无论如何一定会执行的语句
    print(" --- Finally --- ")


separator("module")
# module name 可以省略后缀
# from testModule import putMsg   -> putMsg() 可以省略模块前缀
# or from testModule import *  -> disadvantage: 可能会导致不同模块间的同名函数覆盖
import testModule
from testModule1 import *
from testModule2 import hello

testModule.putMsg()
hello()  # testModule2
# testModule1.hello()  NameError: name 'testModule1' is not defined


separator("End")