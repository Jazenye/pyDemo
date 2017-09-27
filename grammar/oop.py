# 定义类, 类名推荐大驼峰命名
class Person:

    # 属性
    age = 18
    sex = "male"
    num = 0

    # 私有属性, 变量名前面加上两个下划线
    __money = 100

    # 构造函数, “构造器”方法， 用来初始化
    def __init__(self, name):
        self.name = name
        print("I'm constructor of ", name)

    # 析构函数
    def __del__(self):
        print("I'm destructor of ", self.name)

    # 方法, self 作为第一个参数用来接收对象, 指向实例对象本身，
    # 也是实例方法， 通过类对象没法直接调用实例方法, Error: Person.setAge()
    def setAge(self, age):
        self.age = age
    def showName(self):
        print("My name is : %s " % self.name)
    def showMoney(self):  # 对象内部修改私有变量
        print("money: %d" % self.__money)

    # 私有方法， 外部同样无法访问, 只能在类内部调用
    def __setSex(self):
        pass

    @classmethod  # 类方法, cls 开头(class) 可以修改类属性
    def setNum(cls, num):
        cls.num = num  # Person.setNum(1), 但实例不调用类方法

    @classmethod  # 用类方法一次性创建多个实例
    def createEx(cls, num):  # Person.createEx(3)
        exList = []
        for i in range(num):
            exList.append(Person())
        return exList

    @staticmethod  # 静态方法， 可以没有参数
    def print():  # 实例对象和类对象都可以直接调用
        pass

# 创建类, 不同类的实例， 传入参数给构造函数 __init__
zhangsan = Person("张三")
lisi = Person("李四")

# 调用方法, 私有方法无法被读取 即使是 zhangsan.__setSex("male")
zhangsan.setAge(99)
zhangsan.showName()

# 读取属性, 私有属性无法被读取
# zhangsan.__money -> AttributeError: 'Person' object has no attribute '__money'
print(zhangsan.age)


# 继承父类 Person , 多继承可以通过元组传入多个参数 class Child(Parent1, Parent2):
# 多继承中， 对于同名函数 继承第一个父类 Parent1
# 会继承构造函数和析构函数, 私有属性和方法不会被继承
class Child(Person):

    def showName(self):   # overload
        print("I'm child nameed: ", self.name)


c = Child("child")
c.showName()


# property test
class Test():
    def __init__(self):
        self.__num = 100
        self.__age = 0

    def setNum(self, num):
        print("--- set num ---")  # python2.7 不显示该行
        self.__num = num

    def getNum(self):
        print("--- get num ---")
        return self.__num

    num = property(getNum, setNum)  # 先写get，再写set  并且不能写小括号

    @property  # 装饰器的属性方法, 这里相当于原来的get
    def test(self):
        print("--- age getter ---")
        return self.__age

    @test.setter  # 注意这里是set， 由装饰器的名称体现
    def test(self, value):  # 而函数名称还是相同的
        print("--- age setter ---")
        self.__age = value


t = Test()

t.num = 200  # --- set num ---
print(t.num)

t.test = 10  # --- age setter ---
print(t.test)