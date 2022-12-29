def decorator_function(any_func):
    def wrapper_func():
        print('this is awesome function')
        any_func()
    return wrapper_func
@decorator_function
def func1():
    print('this is function 1')
func1()


def func2():
    print('this is funtion 2')
func2()