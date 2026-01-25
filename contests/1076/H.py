import sys
from collections import deque
sys.setrecursionlimit(500000)
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    if n == 1:
        if a[1] % 2 == 1:
            print("YES")
            print(1)
        else:
            print("NO")
        continue

    adj = [set() for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)

    p = [x % 2 for x in a]

    neighbor_parity_sum = [0] * (n + 1)
    degree = [0] * (n + 1)
    for v in range(1, n + 1):
        for u in adj[v]:
            neighbor_parity_sum[v] += p[u]
        degree[v] = len(adj[v])

    removed = [False] * (n + 1)
    result = []
    found = False

    def can_remove(v):
        return (p[v] + neighbor_parity_sum[v]) % 2 == 1

    def backtrack():
        global found
        if found:
            return

        if len(result) == n:
            found = True
            return

        candidates = []
        for v in range(1, n + 1):
            if not removed[v] and can_remove(v):
                candidates.append((degree[v], v))

        candidates.sort()

        for _, v in candidates:
            if found:
                return
            if removed[v] or not can_remove(v):
                continue

            removed[v] = True
            result.append(v)
            neighbors = list(adj[v])
            for u in neighbors:
                if not removed[u]:
                    neighbor_parity_sum[u] -= p[v]
                    degree[u] -= 1

            backtrack()

            if found:
                return

            result.pop()
            removed[v] = False
            for u in neighbors:
                if not removed[u]:
                    neighbor_parity_sum[u] += p[v]
                    degree[u] += 1

    backtrack()

    if found:
        print("YES")
        print(*result)
    else:
        print("NO")
