def outer_fun():
    def Inner_fun():
        print('inside inner fun')
    return inner_fun
var = outer_fun()
var()

def outer_fun2():
    def inner_fun2():
        print(f"message is {msg}")
    return inner_fun2
var2 = outer_fun2("hi there")
var2()
