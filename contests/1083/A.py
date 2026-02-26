t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    max_index = p.index(n)
    
    if max_index != 0:
        p[0], p[max_index] = p[max_index], p[0]
    
    print(*p)