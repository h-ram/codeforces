t = int(input())

for i in range(t):
    n, s, x = map(int, input().split())
    array = list(map(int, input().split()))

    sum_ = sum(array)
    if sum_ <= s and (s - sum_) % x == 0:
        print("YES")
    else:
        print("NO")
