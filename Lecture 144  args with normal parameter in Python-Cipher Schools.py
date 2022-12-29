def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(1,2,3,4))