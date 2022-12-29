class Laptop:
    dis=50
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    def apply_dis(self):
        off_price = (self.dis/100)*self.price
        return self.price-off_price

laptop1=Laptop('hp','victus',110000)
laptop1.dis = 50
print(laptop1.name)
print(laptop1.__dict__)
print(laptop1.apply_dis())