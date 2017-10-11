def putMsg():
    print("I'm module from testModule!!!")

def test():
    print("test this module")

# 变量: __name__ 在该文件执行则为 __main__
# 如果外部调用该文件，则 __name__ == tesstModule  不会调用测试部分的内容
if __name__ == '__main__':
    print("--- in. test ---")
    test()
    print("--- out. test ---")

