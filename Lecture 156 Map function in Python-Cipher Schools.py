num = [1,2,3,4]
def square(a):
    return a**2
print(list(map(square,num)))

num = [1,2,3,4]
print(list(map(lambda a:a**2,num)))

sq = [i**2 for i in num]
print(sq)
