t = int(input())
for _ in range(t):
    n = int(input())
    temp = n
    k = 1
    d = 2
    
    while d * d <= temp:
        if temp % d == 0:
            k *= d
            while temp % d == 0:
                temp //= d
        d += 1
    
    if temp > 1:
        k *= temp
    
    print(k)
