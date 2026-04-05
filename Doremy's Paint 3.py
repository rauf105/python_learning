t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split))
    from collections import Counter

    freq = Counter(a)

    if len(freq) == 1:
        print("Yes")

    elif len(freq) == 2:
        value = list(freq.values())
        if abs(value[0] - value[1]) <=1 :
            print("Yes")
        else:
            print("No")
    else:
        print("No")