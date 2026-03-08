def waterfill(state, extra):
    asc = state[::-1]
    level = 0
    length = len(asc)

    while level + 1 < length:
        need = (asc[level + 1] - asc[level]) * (level + 1)
        if need > extra:
            break
        extra -= need
        for i in range(level + 1):
            asc[i] = asc[level + 1]
        level += 1
    incrament, remaining = divmod(extra, level + 1)
    for i in range(level + 1):
        asc[i] += incrament
    for i in range(remaining):
        asc[i] += 1
    asc.sort()
    return asc[::-1]


t = int(input())
for _ in range(t):
    n, m, l = map(int, input().split())
    a = list(map(int, input().split()))

    spaces = [a[0]]
    for i in range(1, n):
        spaces.append(a[i] - a[i - 1])

    spaces.append(l - a[-1])
    remainingaining = n
    width = min(m, remainingaining + 1)
    state = [0] * width
    for gap in spaces[:-1]:
        state = waterfill(state, gap)
        remainingaining -= 1
        next_width = min(m, remainingaining + 1)
        state = state[1:]
        while len(state) < next_width:
            state.append(0)

    print(state[0] + spaces[-1])