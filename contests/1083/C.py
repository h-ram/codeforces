import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    blogs = []
    occ = {}
    for _ in range(n):
        row = list(map(int, input().split()))
        a = row[1:]
        s = set()
        b = []
        for x in reversed(a):
            if x not in s:
                s.add(x)
                b.append(x)
        blogs.append(b)

    for i in range(n):
        for x in blogs[i]:
            occ.setdefault(x, []).append(i)

    seen = set()
    used = [False] * n
    ans = []
    key = [None] * n
    pq = []

    for i in range(n):
        key[i] = tuple(blogs[i])
        heapq.heappush(pq, (key[i], i))

    picked = 0
    while picked < n:
        while True:
            k, i = heapq.heappop(pq)
            if not used[i] and k == key[i]:
                break

        used[i] = True
        picked += 1

        changed = set()
        for x in blogs[i]:
            if x in seen:
                continue
            seen.add(x)
            ans.append(x)
            for j in occ.get(x, []):
                if not used[j]:
                    changed.add(j)

        for j in changed:
            key[j] = tuple(v for v in blogs[j] if v not in seen)
            heapq.heappush(pq, (key[j], j))

    print(*ans)