a = "b'\\xe3\\x80\\x82'"
b = '\\u4eca\\u5929\\u5929\\u6c14\\u4e0d\\u9519'
c = a[2:-1].encode()
e = [aa for aa in c]
d = bytes(e)
print(d.decode("utf-8"))