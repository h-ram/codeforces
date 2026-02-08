t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    if w == 1:
        print(0)
    else:
        blocks = n // w
        rem = n % w
        print(blocks * (w - 1) + min(rem, w - 1))

