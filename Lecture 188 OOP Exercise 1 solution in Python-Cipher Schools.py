class Laptop:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price

laptop1=Laptop('hp','victus',110000)
print(laptop1.name)