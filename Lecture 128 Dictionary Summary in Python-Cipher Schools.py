d = {'name' : 'aniket', 'age' : 17}
d1= dict(name = 'aniket', age = 17)
d2 = {
    'name' : 'aniket',
    'age' : 17
}
print(d['name'])

empty_dict = {}
empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'
print(empty_dict)

for key,value in d.items():
    print(f'key is {key} : value is {value}')
for i in d:
    print(i)
for j in d.items():
    print(j)
print(d.get('name'))
print(d.pop('name'))
print(d)
