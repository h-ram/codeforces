t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    is_sorted = True
    for i in range(n - 1):
        if a[i] > a[i+1]:
            is_sorted = False
            break
            
    if is_sorted:
        print(n)
    else:
        print(1)
