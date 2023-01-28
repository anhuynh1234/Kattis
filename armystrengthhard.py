import copy

cases_numb = int(input())

cases = []
case = []

for _ in range(cases_numb):
    blank = input()
    case.append(list(map(int, input().split())))
    case.append(list(map(int, input().split())))
    case.append(list(map(int, input().split())))
    cases.append(copy.deepcopy(case))
    case = []

for k in cases:
    ng = k[0][0]
    nm = k[0][1]
    god = k[1]
    god.sort(reverse=True)
    mecha = k[2]
    mecha.sort(reverse=True)
    while len(god) > 0 and len(mecha) > 0:
        if god[-1] > mecha[-1]:
            mecha.pop()
        elif mecha[-1] > god[-1]:
            god.pop()
        else:
            mecha.pop()
    if len(god) > 0:
        print("Godzilla")
    else:
        print("MechaGodzilla")
