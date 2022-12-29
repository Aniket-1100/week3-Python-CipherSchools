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
class Smartphone2(Smartphone):
    def __init__(self,brand,name,price,ram,storage,rear_cam,front_camera):
        super.__init__(brand,name,price,ram,storage,rear_cam)
        self.front_camera=front_camera
    def full_name(self):
        return f"{self.brand} {self.name} and price is {self.price} and front cam is {self.front_camera}"
    

phone = Phone('nokia','1100',1000)
phone2 = Smartphone('oneplus','10',40000,'8gb','32mp')
phone3 = Smartphone2('oneplus','9',36000,'8gb','64mp','16mp')
print(phone3.full_name() + f"and price is {phone3.price}")
print(isinstance(oneplus9,Smartphone2))
