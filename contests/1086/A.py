from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    counter = Counter()
    for i in range(n):
        row = list(map(int, input().split()))
        counter.update(row)
    print("NO" if counter.most_common(1)[0][1] > n*n - n else "YES")
