from functools import wraps
def only_data_type(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print("Invalid arguments")
        return wrapper
    return decorator

@only_data_type(str)
def string(*args):
    string=""
    for i in args:
        string+=i
    return string
print(string('aniket','singh'))
