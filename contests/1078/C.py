t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    strips = [input().strip() for _ in range(k)]
    
    available = [set(strips[j][i] for j in range(k)) for i in range(n)]
    for d in range(1, n + 1):
        if n % d != 0:
            continue
        pattern = []
        valid = True
        
        for r in range(d):
            common = available[r]
            for pos in range(r + d, n, d):
                common = common & available[pos]
                if not common:
                    break
            
            if not common:
                valid = False
                break
            pattern.append(next(iter(common)))
        if valid:
            print(''.join(pattern) * (n // d))
            break