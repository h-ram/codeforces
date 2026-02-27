
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))
    
    A = p[:x]
    B = p[x:y]
    C = p[y:]
    S = A + C
    
    if not B:
        print(*p)
        continue
        
    minim_value = min(B)
    minim_index = B.index(minim_value)
    B_min = B[minim_index:] + B[:minim_index]
    
    k = len(S)
    for i in range(len(S)):
        if B_min[0] < S[i]:
            k = i
            break
            
    anser = S[:k] + B_min + S[k:]
    print(*anser)
