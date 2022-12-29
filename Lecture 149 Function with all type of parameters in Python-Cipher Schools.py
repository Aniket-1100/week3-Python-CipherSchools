def func(name='unknown',age=17):
    print(name)
    print(age)
func('harshit')


def func1(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func1('harshit',1,2,3,a=1,b=2)