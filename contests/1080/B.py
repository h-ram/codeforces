t = int(input())
for _ in range(t):
    n = int(input())
    perm = list(map(int, input().split()))
    
    previous_perm = []
    while previous_perm != perm:
        previous_perm = perm.copy()
        for i in range(1, n // 2 + 1):
            pos_i = i - 1
            pos_2i = 2 * i - 1
            
            if perm[pos_i] > perm[pos_2i]:
                perm[pos_i], perm[pos_2i] = perm[pos_2i], perm[pos_i]
    
    if perm == sorted(perm):
        print("YES")
    else:
        print("NO")