t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prefix_b = [0] * (n + 1)
    for i in range(n):
        prefix_b[i + 1] = prefix_b[i] + b[i]

    sorted_a = sorted(a, reverse=True)

    candidates = []
    prev = -1
    for i, val in enumerate(sorted_a):
        if val != prev:
            candidates.append((val, i + 1))
            prev = val
        else:
            candidates[-1] = (val, i + 1)

    best_score = 0

    for x, count in candidates:
        total_swords = count

        lo, hi = 0, n
        levels = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if prefix_b[mid] <= total_swords:
                levels = mid
                lo = mid + 1
            else:
                hi = mid - 1

        score = x * levels
        best_score = max(best_score, score)

    print(best_score)
