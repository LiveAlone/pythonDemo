
def set_age(self, age):
    self.age = age


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self._score = score

    def print_student(self):
        print 'name %s, age: %s, score: %s ' % (self.name, self.age, self._score)

    # def print_none_field(self):
    #     print 'none field %s' % self.field

yao = Student('yao', 20, 100)
qi = Student('qi', 30, 100)
yao.print_student()
# qi.print_student()

# jun = Student('jun', 100)
# jun.field = 'hehe'
# jun.print_none_field()

# print yao.name
# print yao.__score

from types import MethodType
yao.set_age = MethodType(set_age, yao, Student)
yao.set_age(99)
print yao.print_student()


# __slots__ only attribute

