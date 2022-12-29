def decorator_function(any_func):
    def wrapper_func(*args,**kwargs):
        print('this is awesome function')
        return any_func(*args,**kwargs)
    return wrapper_func
@decorator_function
def func1():
    print('this is function 1 with arguement {a}')
func1(7)

@decorator_function
def func2(a,b):
    return a+b
print(func2(2,3))

