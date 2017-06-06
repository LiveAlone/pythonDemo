# from collections import Iterable
# import os

# slice condition
# L = ['yao', 'qi', 'jun', 'test', 'hehe', 'condition', 'da', 'bin']
# print L

# for i in range(3):
#     print L[i]

# print L[1: 3]
# print L[-1:]
# print L[-2:]
# print L[-3: -1]
# print L[:]

# Lint = range(100)
# print Lint
# print Lint[::5]

# tuple config
# print (0, 1, 2, 3, 4, 5)[:3]
# print 'ABCDSRERASDGFASDF'[:3]


# for instance iteration config
# d = {'a': 1 , 'b': 2, 'c': 3}
# for key in d:
#     print key
#
# for ch in 'ABC':
#     print ch

# ( for in ) formatter use in Iterable
# print isinstance('ABC', Iterable)
# print isinstance([1, 2, 3], Iterable)
# print isinstance(123, Iterable)

# for i, value in enumerate([1, 2, 3]):
#     print i, value

# for x, y in [(1, 2), (3, 4)]:
#     print x + y

# list generate condition
# print [x * x for x in range(1, 11) if x % 2 == 0]
# print [m + n for m in 'ABCD' for n in 'abcd']
# print [d for d in os.listdir('.')]

# like iterator
# d = {'x': 'X', 'y': 'Y'}
# print isinstance(d.iteritems(), Iterable)
# for s in d.iteritems():
#     print s
# print [k + '=' + v for k, v in d.iteritems()]
# print [k.lower() + '=' + v.lower() for k, v in d.iteritems()]

# x = 'abc'
# y = 123
# print isinstance(x, str)
# print isinstance(y, str)

# key generate condition
# g = (x * x for x in range(10))
# print g.next()
# print g.next()
# print g.next()

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#
# o1 = fib(6)
# o2 = fib(7)
# print o1.next()
# print o2.next()
# print o1.next()
# print o1.next()
# print o2.next()
