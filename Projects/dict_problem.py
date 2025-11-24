print('''Word Grouping Dictionary:
Convert paragraph → words (clean punctuation)
Count frequencies of each word
Group words by starting letter
Sort each group alphabetically using lambda''')
n = (input("Enter a long paragraph String: "))
n = n.split()
d= {}
for i in n:
    if i[0] not in d:
        d[i[0]] = {}
    d[i[0]][i] = d[i[0]].get(i,0)+1
d= dict(sorted(d.items(), key = lambda x: len(x[1]),reverse = True))
s = dict(sorted(d.items() , key = lambda x : sum(x[1].values()),reverse = True))
print("Sorted based on the sum of total Frequenncies: ",s)
print(d)
# apple apple apple boy ball cat cat cat cat
# Sorted based on the sum of total Frequenncies:  {'c': {'cat': 4}, 'a': {'apple': 3}, 'b': {'boy': 1, 'ball': 1}}

