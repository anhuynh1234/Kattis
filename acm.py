import copy
n, p = map(int, input().split())
probs = list(map(int, input().split()))

mins = 0
mins1 = 0
solved = 0

mins += copy.deepcopy(probs[p])
mins1 += copy.deepcopy(probs[p])
if mins > 300:
    print("0 0")
else:
    solved += 1
    del probs[p]
    probs.sort()

    for i in probs:
        mins += i
        if mins <= 300:
            mins1 += mins    
            solved += 1
        else:
            # mins -= mins + 1
            break
    print(str(solved) + " " + str(mins1))
