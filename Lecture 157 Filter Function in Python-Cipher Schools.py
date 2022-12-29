def even(a):
    return a%2==0

num = [1,2,3,4,5,6,7,8]
evens = tuple(filter(even,num))
print(evens)

new_evens=[i for i in num if i%2==0]
print(new_evens)