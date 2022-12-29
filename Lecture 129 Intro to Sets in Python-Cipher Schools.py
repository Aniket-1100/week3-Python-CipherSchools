s = {1,2,3,2}
print(s)
l = [1,2,3,4,5,2,5,3]
s2 = list(set(l))
print(s2)

s.add(4)
s.remove(3)
print(s)
print(s.clear())
s1 = s.copy
print(s1)


