class Phone:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=max(price,0)
        
    def comp(self):
        return f"{self.brand} {self.name} and price {self.price}"
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")
    
    def full_name(self):
        return f"{self.brand} {self.name}"
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self,new_price):
        self.price=max(new_price,0)



phone1 = Phone('nokia','1100',1000)
print(phone1.price)
print(phone1.comp)