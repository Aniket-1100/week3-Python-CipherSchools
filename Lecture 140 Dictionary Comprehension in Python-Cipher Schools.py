square = {f"square of {i} is":i**2 for i in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")

    
string = "Aniket"
word_count = {char:string.count(char) for char in string}
print(word_count)