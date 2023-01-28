alphabet = list("abcdefghijklmnopqrstuvwxyz".upper())

n = int(input())
people = []
for _ in range(n):
    people.append(list(input()))

decreasing = False
increasing = False
neither = False

for i in range(n-1):
    for k in range(min(len(people[i]), len(people[i+1]))):
        if alphabet.index(people[i][k]) > alphabet.index(people[i+1][k]) and increasing == False:
            decreasing = True
            break
        elif alphabet.index(people[i][k]) < alphabet.index(people[i+1][k]) and decreasing == False:
            increasing = True
            break
        elif alphabet.index(people[i][k]) == alphabet.index(people[i+1][k]):
            continue
        else:
            neither = True
            break
    if neither != False:
        break

if neither == False:
    if decreasing == True:
        print("DECREASING")
    elif increasing == True:
        print("INCREASING")
else:
    print("NEITHER")
