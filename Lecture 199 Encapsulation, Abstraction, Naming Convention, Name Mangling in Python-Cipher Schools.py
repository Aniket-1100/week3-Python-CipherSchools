class Phone:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")
    
    def full_name(self):
        return f"{self.brand} {self.name}"
    def send_message(self):
        pass
phone1 = Phone('nokia','1100',1000)
print(phone1.price)

l = [3,4,1,2]
l.sort()
print(l)
