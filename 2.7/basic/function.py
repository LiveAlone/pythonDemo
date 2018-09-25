
# function call
# print abs(-100)
# print cmp(1, 2)
# print int(True)


# def function
# def my_function(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('input type error')
#     if x > 0:
#         pass
#     else:
#         print 'x smaller'

# my_function(-100)
# my_function(100)
# my_function('')


# def multi_return(x, y):
#     return y, x + y
#
# print multi_return(100, 101)


def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city


enroll('test', 1, 7, '123')
# enroll('Sarah', 'F')
# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='Tianjin')

# error,  to not mutable object, default value
# def add_end(L=[]):
#     L.append('END')
#     return L
#
# print add_end()
# print add_end()


# def cal_cul(numbers):
#     result = 0
#     for n in numbers:
#         result = result + n
#     return result
#
# print cal_cul([100, 1])
#
#
# def cal_cul2(*numbers):
#     result = 0
#     for n in numbers:
#         result = result + n
#     return result
#
# print cal_cul2(100, 1)
# print cal_cul2(*[100, 100])

# def func(a, b, c=0, *args, **kw):
#     print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

# func(1, 2)
# func(1, 2, c=3)
# func(1, 2, 3, 'a', 'b')
# func(1, 2, 3, 'a', 'b', x=99)
# kw = {'city': 'Beijing', 'job': 'Engineer'}
# func(1, 2, 3, *[1, 2, 3], **{'city': 'Beijing', 'job': 'Engineer'})


# last difui function
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# print fact(100)
# print fact(200)



