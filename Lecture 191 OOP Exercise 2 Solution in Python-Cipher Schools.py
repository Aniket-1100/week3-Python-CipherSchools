class Laptop:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    def apply_dis(self,num):
        off_price = (num/100)*self.price
        return self.price-off_price

laptop1=Laptop('hp','victus',110000)
print(laptop1.name)
print(laptop1.apply_dis(10))