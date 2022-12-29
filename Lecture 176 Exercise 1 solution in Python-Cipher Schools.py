from functools import wraps
import time
def calc_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"executing ..... {function.__name__}")
        t1 = time.time()
        returned_value=function(*args,**kwargs)
        t2=time.time()
        tot_time=t2-t1
        print(f"this function took {tot_time} seconds")
        return returned_value
    return wrapper

@calc_time
def square(n):
    return [i**2 for i in range(1,n+1)]

square(5)