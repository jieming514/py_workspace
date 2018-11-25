
# 类的使用

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __new__(cls, name, age):
        if 0 < age < 150:
            return object.__new__(cls)
        else:
            return None

    def __str__(self):
        return '%s, %s' % (self.name, self.age)


print(Person('Tom',10))
print(Person('Jack',1222))