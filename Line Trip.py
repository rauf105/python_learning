t = int(input())

for _ in range(t):
    n, x = map(int,input().split())
    a = list(map(int, input().split()))

    prev = 0
    max_dist = 0

    for station in a:
        max_dist = max(max_dist, station - prev)
        prev = station

    max_dist = max(max_dist , 2*(x - a[-1]))
    print(max_dist)    