class Person:
    count_ins = 0

    def __init__(self,fname,lname,age):
        Person.count_ins += 1
        self.fname=fname
        self.lname=lname
        self.age=age
    
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)
    @staticmethod
    def hello():
        print('hello static method called')

    @classmethod
    def count_ins(cls):
        return f"you have created {cls.count_ins} instances of {cls.__name__}"

    def full_name(self):
       return f"{self.fname} {self.lname}" 
    
    def is_above_18(self):
        return self.age>18

p3 = Person.from_string('Harshit,Vashistha,24')
Person.hello()


    