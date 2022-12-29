def even(n):
    for num in range(1,n+1):
        if num%2==0:
            yield num

even_nums=even(20)

for num in even_nums:
    print(num)