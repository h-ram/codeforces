limit = 1000005


min_prime = list(range(limit))
for i in range(2, int(limit**0.5) + 1):
    if min_prime[i] == i:
        for j in range(i * i, limit, i):
            if min_prime[j] == j:
                min_prime[j] = i



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
        print("Bob")
        continue
        
    alice_win = False
    primes = []
    for x in a:
        if x == 1:
            primes.append(1)
            continue
            
        p = min_prime[x]
        temp = x
        while temp % p == 0:
            temp = temp // p
            
        if temp > 1:
            alice_win = True
            break
        else:
            primes.append(p)
    if alice_win:
        print("Alice")
        continue
        
    p_sorted = True
    for i in range(n - 1):
        if primes[i] > primes[i+1]:
            p_sorted = False
            break
    if p_sorted:
        print("Bob")
    else:
        print("Alice")
