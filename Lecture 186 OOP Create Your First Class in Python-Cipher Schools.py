class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

p1=Person('Aniket','Singh',18)
p2=Person('Harshit','Vashistha',24)
print(p1.fname)
print(p2.fname)