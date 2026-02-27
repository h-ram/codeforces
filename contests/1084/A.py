t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_ = max(arr)
    maxes = [1 for num in arr if num == max_]
    print(len(maxes))