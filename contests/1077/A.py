t = int(input())
for _ in range(t):
    n = int(input())
    perm = list(range(1, n + 1))
    for i in range(n - 1, 0, -1):
        perm[:i+1] = perm[:i+1][::-1]
    print(*perm)