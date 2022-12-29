def nums(n):
    for i in range(1,n+1):
        yield i
print(nums(10))

number= nums(10)


for num in number:
    print(num)