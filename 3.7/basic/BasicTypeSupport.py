#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 支持 double 精度，多常亮配置方式
# print(10 / 3)

# 整数类型支持
# print(10 // 3)

# 不同数据类型
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# 不同编码方式支持
# print('包含中文的str')
# print(ord('A'))
# print(ord('中'))
# print(chr(25991))
# print('中文'.encode('utf-8'))

# len() 字符的个数， 注意不是长度， 看下面的例子
# print(len(b'ABC'))
# print(len('ABC'))
#
# print(len('中文'))
# print('中文'.encode('utf-8')) # 其实长度6个
# print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 中文编码后二进制字节
# print(len('中文'.encode('utf-8')))

# 输出字符串格式化方式
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# list tuple 配置方式
# classmates = ['Michael', 'Bob', 'Tracy']
# print(classmates)
# classmates.append('Admin')
# print(classmates)
# classmates.insert(1, 'Jack')
# print(classmates)
# classmates.pop(1)
# print(classmates)
# print(len(classmates))

# t = (1 ,)
# print(t)

# t = ('a', 'b', ['A', 'B'])
# print(t[2][0])

# judge condition validate
# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

# loop for range select
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# break continue
# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n += 1
# print('END')
#
# n = 0
# while n < 10:
#     n += 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

# dict set 集合的处理配置方式
# dict 类似 map 的数据结构格式, 叫做字典 存储方式 加快查询方式
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])
# d['Adam'] = 67
# print(d)
# print('Thomas' in d)
# print('Bob' in d)
# # 通过 get 方式 ， 返回 None 默认数值
# print(d.get('Toms'))
# print(d.get('Toms', -1))
#
# # key = [1, 2, 3]
# # d[key] = 'ABC'  # error key hash changed

# set 集合操作方式
s = set([1, 1, 2, 2, 3, 3])
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)







