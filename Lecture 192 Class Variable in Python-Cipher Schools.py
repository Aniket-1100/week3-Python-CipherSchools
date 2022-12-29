class Circle:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def clac_circum(self):
        return 2*Circle.pi*self.r
    def calc_area(self):
        return Circle.pi*(self.r**2)
c = Circle(5)
print(c.clac_circum())
print(c.calc_area())