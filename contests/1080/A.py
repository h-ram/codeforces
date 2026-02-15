t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if 67 in arr:
        print("YES")
    else:
        print("NO")

# the number 67 is a prime number, it can only be reached with 1x67.