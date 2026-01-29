t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    total = s.count('1')
    gaps = s.split('1')
    for i, gap in enumerate(gaps):
        k = len(gap)
        if k == 0:
            continue
        if len(gaps) == 1:  
            total += (k + 2) // 3
        elif i == 0:  
            total += (k + 1) // 3
        elif i == len(gaps) - 1:  
            total += (k + 1) // 3
        else: 
            total += k // 3
    print(total)