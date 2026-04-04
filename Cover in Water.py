t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    count = 0
    i = 0

    while i < n:
        if s[i] == '.':
            length = 0
            
            # count continuous dots
            while i < n and s[i] == '.':
                length += 1
                i += 1
            
            # if segment >= 3 → answer = 2
            if length >= 3:
                count = 2
                break
            else:
                count += length
        else:
            i += 1

    print(count)