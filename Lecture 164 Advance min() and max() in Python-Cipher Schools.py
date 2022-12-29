def func(item):
    return len(item)

names = ['Harshit','Aniket','ab']
print(max(names,key=func))
print(min(names,key=func))

names = ['Harshit','Aniket','ab']
print(max(names,key= lambda item: len(item)))

student = {
    'harshit' : {'score':90, 'age':24},
    'mohit' : {'score':60, 'age':19},
    'rohit' : {'score':70, 'age':25}
}
print(max(student,key = lambda item: student[item]['age']))

student2 = [
    {'name':'harshit', 'score':90, 'age':24},
    {'name':'mohit', 'score':60, 'age':19},
    {'name':'rohit,', 'score':70, 'age':25}
]
print(max(student2, key = lambda item:item.get('score'))['name'])