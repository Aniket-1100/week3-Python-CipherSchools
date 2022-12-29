d={'a':1,'h':2,'h':3}
print(d)

def word_counter(s):
    count={}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter('harshit'))