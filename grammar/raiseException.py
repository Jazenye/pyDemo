class ShortInputException(Exception):  # 继承异常
    # 定义异常类
    def __init__(self, length, atleat):  # 重写构造函数
        Exception.__init__(self)
        self.length = length
        self.atleast = atleat

try:
    string = input("请输入一个长度大于3的字符串： ")

    if len(string) < 3:
        # raise 引发一个自定义的异常, 会被 except ShortInputException 捕获
        raise ShortInputException(len(string), 3)  # 创建对象, 调用构造函数
except EOFError:  # 捕获异常
    print("\n 你输入了一个结束标记EOF")
except ShortInputException as errObj:  # errObj 被绑定到了错误的实例
    print("ShortInputException： 输入的长度是 %d, 长度至少是: %d" % (errObj.length, errObj.atleast))
else:
    print("NO ERROR")
