t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    contributions = [bank // x * y for bank in a]
    total_given = sum(contributions)

    max_money = 0
    for i in range(n):
        temp_money = a[i] + (total_given - contributions[i])
        max_money = max(max_money, temp_money)

    print(max_money)