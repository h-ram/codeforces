t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    l = 0
    while l < n and p[l] == n - l:
        l += 1

    if l == n:
        print(*p)
        continue

    max_val = max(p[l:])
    r = p.index(max_val, l)

    p[l:r+1] = p[l:r+1][::-1]
    print(*p)
