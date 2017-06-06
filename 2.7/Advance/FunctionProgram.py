
# function programming
# f = abs
# print f(-100)


# def function_add(x, y, f):
#     return f(x) + f(y)

# print function_add(1, -2, abs)

# map reduce
# def f(x):
#     return x*x
#
# print map(f, [1, 2, 3, 4])
# print map(str, [1, 2, 3, 4])


# def add(x, y):
#     return x + y

# print reduce(add, [1, 2, 3, 4, 5])

# filter config
# def not_empty(s):
#     return s and s.strip()
#
# print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

# sort config
# print sorted([36, 5, 12, 9, 21])
#
#
# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0
#
# print sorted([36, 5, 12, 9, 21], reversed_cmp)

# return function

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print f1 == f2
# print f1()
# print f2()


# single object condition
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i * i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print f1()
# print f2()
# print f3()


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(j=i):
#             return j * j
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print f1()
# print f2()
# print f3()

# def build(x, y):
#     return lambda: x * x + y * y
#
# print build(1, 2)()
#
# func = lambda x, y: x * x + y * y
# print func(1, 2)


# function decorator
# def log(func):
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print '2013-12-25'

# f = now
# f()
# print now.__name__
# now()


# easy decoretor
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print '2013-12-25'
#
# now()

