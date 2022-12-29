num = list(range(1,11))
n = []
for i in num:
    if i%2==0:
        n.append(i)
print(n)

even_nums = [ i for i in num if i%2==0 ]
print(even_nums)