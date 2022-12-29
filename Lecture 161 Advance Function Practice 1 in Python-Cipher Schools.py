def average(*args):
    avg=[]
    for i in zip(*args):
        avg.append(sum(i)/len(i))
    return avg
print(average([1,2,3],[4,5,6],[7,8,9]))

a = lambda *args : [sum(i)/len(i) for i in zip(*args)]
print(a([1,2,3],[4,5,6],[7,8,9]))