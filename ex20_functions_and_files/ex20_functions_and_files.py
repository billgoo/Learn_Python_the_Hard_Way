from sys import argv

# script, input_file = argv
script, input_file = "ex20_functions_and_files/ex20.py", "ex20_functions_and_files/test.txt"

def print_all(f):
    print(f.read())

# 如果不倒带，文件读完就是空的了，也就是为什么24行打印出来是空的
# 读文件相当于有个全局指针向后走
def rewind(f):
    '''
    概述
        seek() 方法用于移动文件读取指针到指定位置。
    语法
        seek() 方法语法如下：
            fileObject.seek(offset[, whence])
    参数
        offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
        whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
    返回值
        如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
    '''
    f.seek(0)

def print_a_line(line_count, f):
    # print(line_count, f.readline())
    print(line_count, f.readline(), end="")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# print(current_file.read())
rewind(current_file)
# print(current_file.read())

print("Let's print three lines:")

'''
Why are there empty lines between the lines in the file? The readline() function returns the \n
that’s in the file at the end of that line. Add a end = "" at the end of your print function calls
to avoid adding double \n to every line.
'''
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
