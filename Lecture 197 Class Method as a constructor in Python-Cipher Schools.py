class Person:
    count_ins=0
    def __init__(self,fname,lname,age):
        Person.count_ins += 1
        self.fname=fname
        self.lname=lname
        self.age=age
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_ins(cls):
        return f"you have created {cls.count_ins} instances of {cls.__name__} "
    def full_name(self):
        return f"{self.fname} {self.lname}"

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit','Vashistha',18)
p3 = Person.from_string('Aniket,Singh,17')
print(p3.full_name())