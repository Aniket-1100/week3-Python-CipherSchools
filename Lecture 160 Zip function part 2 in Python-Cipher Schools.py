
l = [(1,2),(3,4),(5,6),(7,8)]
l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))

newlist=[]
for i in zip(l1,l2):
    newlist.append(max(i))