class Phone:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")
    
    def full_name(self):
        return f"{self.brand} {self.name}"
class Smartphone(Phone):
    def __init__(self,brand,name,price,ram,storage,rear_cam):
        super.__init__(brand,name,price)
        self.ram=ram
        self.storage=storage
        self.rear_cam=rear_cam

phone = Phone('nokia','1100',1000)
phone2 = Smartphone('oneplus','10',40000,'8gb','32mp')
print(phone.full_name())
print(phone2.full_name() + f"and price is {phone.price}")

