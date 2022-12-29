fruits = ['grapes','apple','mango']
fruits.sort
print(fruits)

fruits2 = ['grapes','apple','mango']
print(sorted(fruits2))

guitars = [
    {'model1': 'yamaha f310', 'price': 8400},
    {'model2': 'faith neptune', 'price': 50000},
    {'model3': 'faith apollo venus', 'price': 35000},
    {'model4': 'taylor 814ce', 'price': 450000},
]

sorted_guitrs = sorted(guitars, key = lambda d :d['price'], reverse = True)
print(sorted_guitrs)
