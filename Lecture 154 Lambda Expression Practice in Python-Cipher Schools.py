def is_even(a):
    return a%2==0
print(is_even(6))

b = lambda x : x%2==0
print(b(6))

def last_char(s):
    return s[-1]
print(last_char('harshit'))

last = lambda z : z[-1]
print(last('aniket'))

def func(s):
    if len(s)>5:
        return True
    return False

func = lambda s: True if len(s)>5 else False
print(func('abcdefg'))
