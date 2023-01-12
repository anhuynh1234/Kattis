n, m = map(int, input().split())

rankings = []
for i in range(n):
    rankings.append('T'+str(i+1))
matches = []
for _ in range(m):
    matches.append(list((input().split())))

for k in matches:
    if rankings.index(k[0]) > rankings.index(k[1]):
        rankings.insert(rankings.index(k[0])+1, k[1])
        rankings.remove(k[1])
    else:
        continue
print(" ".join(rankings))

pass