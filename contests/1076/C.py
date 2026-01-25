t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    suffix_max_a = [0] * n
    suffix_max_b = [0] * n

    suffix_max_a[n-1] = a[n-1]
    suffix_max_b[n-1] = b[n-1]

    for i in range(n-2, -1, -1):
        suffix_max_a[i] = max(suffix_max_a[i+1], a[i])
        suffix_max_b[i] = max(suffix_max_b[i+1], b[i])

    c = [0] * n
    for i in range(n):
        c[i] = max(suffix_max_a[i], suffix_max_b[i])

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + c[i]

    results = []
    for _ in range(q):
        l, r = map(int, input().split())
        results.append(prefix[r] - prefix[l-1])

    print(*results)
