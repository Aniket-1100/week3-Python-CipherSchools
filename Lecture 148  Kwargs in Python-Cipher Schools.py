def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

d={'name':'aniket','age':17}
func(**d)