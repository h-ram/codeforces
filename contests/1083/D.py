import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    left = [-1] * n
    right = [-1] * n
    parent = [-1] * n
    stack = []

    for i, x in enumerate(a):
        last = -1
        while stack and a[stack[-1]] < x:
            last = stack.pop()
        if stack:
            p = stack[-1]
            parent[i] = p
            right[p] = i

        if last != -1:
            parent[last] = i
            left[i] = last
        stack.append(i)

    root = stack[0]
    while parent[root] != -1:
        root = parent[root]
    height = 0
    st = [(root, 1)]
    while st:
        u, d = st.pop()
        if d > height:
            height = d
        lu = left[u]
        if lu != -1:
            st.append((lu, d + 1))
        ru = right[u]
        if ru != -1:
            st.append((ru, d + 1))

    print(n - height)
