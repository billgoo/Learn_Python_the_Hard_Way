# create a mapping of state to abbreviation
"""
states = {
    'Beijing': 'BJ',
    'Fujian': 'FJ',
    'Zhejiang': 'ZJ',
    'Shanghai': 'SH',
    'Jiangsu': 'JS'
}
"""
"""
states = dict([
    ('Beijing', 'BJ'),
    ('Fujian', 'FJ'),
    ('Zhejiang', 'ZJ'),
    ('Shanghai', 'SH'),
    ('Jiangsu', 'JS')
])
"""
# if keys are simple strings
states = dict(
    Beijing= 'BJ',
    Fujian= 'FJ',
    Zhejiang= 'ZJ',
    Shanghai= 'SH',
    Jiangsu= 'JS'
)

# create a basic set of states and some cities in them
cities = {
    'ZJ': 'Hangzhou',
    'JS': 'Suzhou',
    'FJ': 'Xiamen'
}

# add some more cities
cities['SH'] = 'Shanghai'
cities['BJ'] = 'Beijing'

# print out some cities
print('-' * 10)
print("SH State has: ", cities['SH'])
print("BJ State has: ", cities['BJ'])

# print some states
print('-' * 10)
print("Jiangsu's abbreviation is: ", states['Jiangsu'])
print("Fujian's abbreviation is: ", states['Fujian'])

# do it by using the state then cities dict
print('-' * 10)
print("Jiangsu has: ", cities[states['Jiangsu']])
print("Fujian has: ", cities[states['Fujian']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Hubei')

if not state:
    print("Sorry, no Hubei.")

# get a city with a default value
city = cities.get('HB', 'Does Not Exist')
print(f"The city for the state 'HB' is: {city}")

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)


""" collections """

'''
defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。
如果希望key不存在时，返回一个默认值，就可以用defaultdict：
注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
# output
# 'abc'
print(dd['key2']) # key2不存在，返回默认值
# output
# 'N/A'

'''
OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：
'''
from collections import OrderedDict
d = dict([('a', 1), ('c', 3), ('b', 2)])
print(d) # dict的Key是无序的
# output
# {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od) # OrderedDict的Key是有序的
# output
# OrderedDict([('a', 1), ('c', 3), ('b', 2)])
'''
注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
'''
d = dict()
d['z'] = 1
d['y'] = 3
d['x'] = 2
print(d)
# output
# {'z': 1, 'y': 3, 'x': 2}
od = OrderedDict()
od['z'] = 1
od['y'] = 3
od['x'] = 2
print(od.keys()) # 按照插入的Key的顺序返回
# output
# ['z', 'y', 'x']

