from collections import defaultdict

array = [1,1,4,6]

d = defaultdict(lambda:'hi')
for a in array:
    d[a] += 'a'
print(d)

for k in d.values():
    print k