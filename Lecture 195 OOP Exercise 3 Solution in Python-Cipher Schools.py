class Person:
    count_ins=0
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit','Vashistha',18)
p3 = Person('Aniket','Singh',17)
print(Person.count_ins())