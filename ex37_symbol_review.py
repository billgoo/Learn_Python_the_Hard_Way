#%%
""" Keywords """

#%%
''' and '''
True and False == False

#%%
'''
as
with X as Y:
    pass
assign X to Y with enter and leave the block with exit
https://www.jianshu.com/p/1a02a5b63c88
'''

class Sample1:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"
 
    def __exit__(self, type, value, trace):
        print("In __exit__()")
 
def get_sample():
    return Sample1()
 
with get_sample() as sample:
    print("sample:", sample)

# output
# In __enter__()
# sample: Foo
# In __exit__()

class Sample2:
    def __enter__(self):
        return self
 
    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        print("trace:", trace)
 
    def do_something(self):
        bar = 1/0
        return bar + 10
 
with Sample2() as sample:
    sample.do_something()

# output
# type: <type 'exceptions.ZeroDivisionError'>
# value: integer division or modulo by zero
# trace: <traceback object at 0x1004a8128>
# Traceback (most recent call last):
#   File "./with_example02.py", line 19, in <module>
#     sample.do_something()
#   File "./with_example02.py", line 15, in do_something
#     bar = 1/0
# ZeroDivisionError: integer division or modulo by zero

#%%
'''
assert
ensure that is true
'''
assert False, "Error!"

#%%
''' del '''
a = {"a":"b", 2:"e"}
del a[2]
print(a)
# output
# {'a': 'b'}

x = 1
del x
x
# output
# 1

x = ["a", "b"]
y = x
del x
y
# output
# ["a", "b"]

#%%
''' except '''
try:
    pass
except ValueError as identifier:
    print(identifier)

#%%
'''
exec
run a script as python
'''
exec("print('hello')")
exec("""
print('a')
print('b')
""")

#%%
'''
finally
如果try中没有异常，那么except部分将跳过，执行else中的语句。
（前提是try里没有返回值）
finally是无论是否有异常，最后都要做的一些事情。
（无论try里是否有返回值）
在含有return的情况下，并不会阻碍finally的执行
（但是会阻碍else）
'''
try:
    pass
except Exception as identifier:
    pass
else:
    pass
finally:
    pass
'''
try:
    print 1
    return 2
finally:
    print 3
    return 4
output 1 3 4
'''

'''
try:
    print 1
    return 2
finally:
    print 3
    # return 4
output 1 3 2
'''

'''
try:
    print 1
    return 2
except:
    return 3
else:
    print 4
    return 5
finally:
    print 6
    # return 7
output 1 6 2
'''

'''
try:
    可以触发异常的语法
except 错误类型1 [as 变量1]
    异常处理语句1
except 错误类型2 [as 变量2]：
        异常处理语句2
except (错误类型3， 错误类型4):
    异常处理语句3
...
except：
    异常处理语句other
else：
    未发生异常语句
finally：
    最终语句
'''

#%%
'''
global
declare a global variable
'''
global x

#%%
'''
is
'''

'''
== 和 is 的区别:
is 判断两个对象是否为同一对象, 是通过id来判断的; 
当两个基本类型数据(或元组)内容相同时, id会相同, 但并不代表a会随b的改变而改变
'''
a = 1
b = 1
a is b
# output
# True

'''
== 判断两个对象的内容是否相同, 是通过调用__eq__()来判断的
'''
a = [1]
b = a
a == b
a is b
# output
# True
# True
c = a.copy()
a == c
a is c
# output
# True
# False

#%%
'''
lambda
anonymous function

语法：lambda argument_list: expression
lambda 函数有输入和输出：
    输入是传入到参数列表argument_list的值，
    输出是根据表达式expression计算得到的值。

例子：
lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
lambda:None；函数没有输入参数，输出是None
lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
lambda **kwargs: 1；输入是任意键值对参数，输出是1
'''

''' 用法： '''
# 将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数
s = lambda y: y ** y; s(3)  # output = 27

# 将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换
# 例如，为了把标准库time中的函数sleep的功能屏蔽(Mock)，我们可以在程序初始化时调用以下代码：
# 这样，在后续代码中调用time库的sleep函数将不会执行原有的功能。
# 例如，执行time.sleep(3)时，程序不会休眠3秒钟，而是什么都不做。
import time
time.sleep=lambda x:None

# 将lambda函数作为其他函数的返回值，返回给调用者
# lambda函数实际上是定义在某个函数内部的函数，称之为嵌套函数，或者内部函数。
# 对应的，将包含嵌套函数的函数称之为外部函数。内部函数能够访问外部函数的局部变量
# return lambda x, y: x+y

# 将lambda函数作为参数传递给其他函数
# 部分Python内置函数接收函数作为参数
filter(lambda x: x % 3 == 0, [1, 2, 3])
# output [3]
sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))
# output [5, 4, 6, 3, 7, 2, 8, 1, 9]
map(lambda x: x+1, [1, 2,3])
# output [2, 3, 4]
# reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
# output '1, 2, 3, 4, 5, 6, 7, 8, 9'

#%%
''' raise '''
raise ValueError("No")

#%%
'''
yield
Pause here and return to caller
'''
# def X(): yield Y; X().next()

#%%
""" Escape Sequences """
print("asf\rasd")
# output
# asf
print("asf\nasd")
# output
# asf
# asd
print("asf\tasd")
# output
# asf   asd
print("asf\vasd")
# output
# asf
#   asd

#%%
"""String Formats"""
# int: %d, %i
# octal number: %o
# unsigned decimal: %u
# hexadecimal: 小写 %x, 大写 %X
# 科学计数法: %e, %E
# 取小数位数：%f, %F
# %g, %G 得到f或e更短的那个
# char: %c

# repr format %r
print("%r" % int)
print("%r" % int == "<type 'int'>")
print("%r" % int == "<class 'int'>")
# output
# <class 'int'>
# False
# True

# string: %s
# 百分号：%%

#%%
"""Operators"""
'''
装饰器
@
'''
# 原型
import time
def showtime1(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))
    return wrapper

def foo1():
    print('foo..')
    time.sleep(3)

foo1 = showtime1(foo1)
foo1()
# output
# foo..
# spend is 3.0058674812316895

# 不带参数的装饰器:(装饰器,被装饰函数都不带参数)
import time
def showtime2(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime2  #foo = showtime(foo)
def foo2():
    print('foo..')
    time.sleep(3)

@showtime2 #doo = showtime(doo)
def doo2():
    print('doo..')
    time.sleep(2)

foo2()
doo2()
# output
# foo..
# spend is 3.0110087394714355
# doo..
# spend is 2.0016164779663086

# 带参数的被装饰的函数
import time
def showtime3(func):
    def wrapper(a, b):
        start_time = time.time()
        func(a,b)
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime3 #add = showtime(add)
def add3(a, b):
    print(a+b)
    time.sleep(1)

@showtime3 #sub = showtime(sub)
def sub3(a,b):
    print(a-b)
    time.sleep(1)

add3(5,4)
sub3(3,2)
# 9
# spend is 1.0106911659240723
# 1
# spend is 1.0015604496002197

# 带参数的装饰器(装饰函数),
# 实际是对原有装饰器的一个函数的封装,并返回一个装饰器(一个含有参数的闭包函数),
# 当使用@time_logger(3)调用的时候,
# Python能发现这一层封装,并将参数传递到装饰器的环境去
import time
def time_logger4(flag = 0):
    def showtime(func):
        def wrapper(a, b):
            start_time = time.time()
            func(a,b)
            end_time = time.time()
            print('spend is {}'.format(end_time - start_time))
            
            if flag:
                print('将此操作保留至日志')

        return wrapper

    return showtime

@time_logger4(2)  #得到闭包函数showtime,add = showtime(add)
def add4(a, b):
    print(a+b)
    time.sleep(1)

add4(3,4)
# output
# 7
# spend is 1.0103132724761963
# 将此操作保留至日志

# 类装饰器:一般依靠类内部的__call__方法
import time
class Foo5(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        start_time = time.time()
        self._func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

@Foo5  #bar = Foo(bar)
def bar5():
    print('bar..')
    time.sleep(2)

bar5()
# output
# bar..
# spend is 2.0081138610839844

##
# 使用装饰器的缺点:
# 位置错误的代码->不要在装饰器之外添加逻辑功能
# 不能装饰@staticmethod 或者 @classmethod已经装饰过的方法
# 装饰器会对原函数的元信息进行更改,比如函数的docstring,__name__,参数列表:
import time
def showtime6(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime6  #foo = showtime(foo)
def foo6():
    print('foo..')
    time.sleep(3)

def doo6():
    print('doo..')
    time.sleep(2)

print(foo6.__name__)
print(doo6.__name__)
# output
# wrapper
# doo
# 由此可以看出,装饰器会对原函数的元信息进行更改,可以使用wraps,进行原函数信息的添加
# 注解:wraps本身也是一个装饰器,他能把函数的元信息拷贝到装饰器函数中
# 使得装饰器函数与原函数有一样的元信息
import time
from functools import wraps
def showtime7(func):

    @wraps(func)    
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime7  #foo = showtime(foo)
def foo7():
    print('foo..')
    time.sleep(3)

def doo7():
    print('doo..')
    time.sleep(2)

print(foo7.__name__)
print(doo7.__name__)
# output
# foo
# doo

# 常用的内置装饰器:
# 1.staticmethod: 类似实现了静态方法 注入以后,可以直接 : 类名.方法
# 2.property:经过property装饰过的函数 不再是一个函数,
# 而是一个property,类似实现get,set方法
@property
def width8(self):
    return self.__width

@width8.setter
def width8(self, newWidth):
    self.__width = newWidth
# 3.classmethod: 与staticmethod很相似,貌似就只有这一点区别:
# 第一个参数需要是表示自身类的 cls 参数，
# 可以来调用类的属性，类的方法，实例化对象等
"""实例方法、静态方法@staticmethod、类方法@classmethod"""
class Student:
    description = "学员统计信息"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def function(self, fun_type):
        return fun_type

    def instance_method(self):          # 实例方法
        use_type = self.function("实例方法")
        print("------%s------" % use_type)
        print(Student.description)
        print(self.name + '_' + str(self.age) + '_' + self.sex)

    @staticmethod           # 静态方法
    def static_method():
        student_info = Student("xiaoxiao", 20, "female")
        use_type = student_info.function("静态方法")
        print("------%s------" % use_type)
        print(Student.description)
        print(student_info.name + '_' + str(student_info.age) + '_' + student_info.sex)

    @classmethod        # 类方法
    def class_method(cls):
        student_info = cls("xiaoming", 23, "male")
        use_type = student_info.function("类方法")
        print("------%s------" % use_type)
        print(Student.description)
        print(student_info.name + '_' + str(student_info.age) + '_' + student_info.sex)

    def call_different_method(self):
        print("------同一类对象中调用实例方法、静态方法、类方法------")
        self.instance_method()
        self.static_method()
        self.class_method()

# 实例方法
Student("xiaohong", 19, "female").instance_method()
# 静态方法
Student.static_method()
# 类方法
Student.class_method()
# 同一类对象中某个函数调用实例/静态/类方法
Student("xiaohong", 19, "female").call_different_method()

#%%

