n = int(input())
e = int(input())

nights = []
for _ in range(e):
    nights.append(list(map(int, input().split())))

nights_all = []

night = []

for k in range(len(nights)):
    del nights[k][0]
    nights[k].sort()
    if 1 in k:
        nights_all.append(k)
    elif 1 not in k:
        for l in k:
            pass
    
