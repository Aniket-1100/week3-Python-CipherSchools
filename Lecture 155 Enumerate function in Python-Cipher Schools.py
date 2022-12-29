names = ['abc','tuv' ,'xyz']
i = 0
for name in names:
    print(f"{i} ----> {name}")
    i += 1

for i,name in enumerate(names):
    print(f"{i} ----> {name}")

def find(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1
names = ['abc','tuv' ,'xyz']
print(find(names,'abc'))