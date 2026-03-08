t = int(input())
for _ in range(t):
    input()
    s = input().strip()
    min_ones = 0
    max_ones = 0

    for block in s.split("00"):
        first_one = block.find("1")
        if first_one == -1:
            continue

        length = block.rfind("1") - first_one + 1
        min_ones += length // 2 + 1
        max_ones += length

    print(min_ones, max_ones)
        