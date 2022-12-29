class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

    def full_name(self):
        return f"{self.fname} {self.lname}"
    def is_above_18(self):
        return self.age>18

p1 = Person('harshit','vashistha',24)
print(p1.full_name)
print(p1.is_above_18())
