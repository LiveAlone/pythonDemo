import types


class Animal(object):
    def run(self):
        print 'Animal is running'


class Dog(Animal):
    def run(self):
        print 'Dog is running'


class Cat(Animal):
    def run(self):
        print 'Cat is running'


def animal_run(animal):
    animal.run()


dog = Dog()
# dog.run()
cat = Cat()
# cat.run()

# print isinstance(dog, Animal)
# print isinstance(cat, Animal)

# animal_run(dog)
# animal_run(cat)
# animal_run(Animal())

# object type config
# print type('123') == types.StringType
# print type(123) == types.IntType

# get object all attr
# print dir(dog)
# print dog.__class__
# print dog.__doc__

# get all attribute
print hasattr(dog, 'run')
getattr(dog, 'run')()
