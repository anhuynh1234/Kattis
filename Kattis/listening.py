
cx, cy, n = map(int, input().split())

devices = []

ranges = []
for _ in range(n):
    ranges.append(list(map(int, input().split())))

for i in ranges:
    x, y, r = i[0], i[1], i[2]
    devices.append(int(((cx - x)**2 + (cy - y)**2)**(1/2) - r))

devices.sort()

if devices[2] > 0:
    print(str(devices[2]))
elif devices[2] <= 0:
    print('0')