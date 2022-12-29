from functools import wraps
def only_int(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        d=[]
        for arg in args:
            d.append(type(arg)==int)
        if all(d):
            return function(*args,**kwargs)
        else:
            return ("Invalid arguments")

@only_int
def add(*args):
    total=0
    for i in args:
        total+=i
    return total

print(add(1,2,3,4,5))
