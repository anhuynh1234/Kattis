import math

t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))
for i in n:
    print(math.ceil(i/400))