squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

s2 = [i**2 for i in range(1,11)]
print(s2)

s3 = []
for i in range(1,11):
    s3.append(-i)
print(s3)

s_neg = [-i for i in range(1,11)]
print(s_neg)

names = ['Harshit','Mohit','Aniket']
new_list = [name[0] for name in names]
print(new_list)

