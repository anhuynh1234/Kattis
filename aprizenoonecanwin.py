n, x = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()

if prices[0] >= x:
    print("1")
else:
    t = 1

    for i in range(1, len(prices)):
        if prices[i] + prices[i-1] <= x:
            t += 1
        elif (prices[i] + prices[i-1]) > x:
            break
    print(str(t))
