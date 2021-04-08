paragraph = "Bob, hit, ball"

banned = ['bob', 'hit']

sentence = list(paragraph)

words = dict()

s = str()
for el in sentence:
    if el.isalpha() or el.isdigit():
        s += el.lower()
    else:
        if s.strip()  == '':
            continue
        elif s not in words and s not in banned:
            words[s] = 0
        elif s in words and s not in banned:
            words[s] += 1
        s = str()

if s not in words and s not in banned:
    words[s] = 0
elif s in words and s not in banned:
    words[s] += 1
        
sort_dict = sorted(list(words.items()), key = lambda x: -x[1])

print(sort_dict[0][0])
        
    