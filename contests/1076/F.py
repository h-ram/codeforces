t = int(input())
for _ in range(t):
    n, ax, ay, bx, by = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    groups = {}
    for i in range(n):
        if x[i] not in groups:
            groups[x[i]] = [y[i], y[i]]
        else:
            groups[x[i]][0] = min(groups[x[i]][0], y[i])
            groups[x[i]][1] = max(groups[x[i]][1], y[i])

    sorted_x = sorted(groups.keys())

    intervals = [(groups[xi][0], groups[xi][1]) for xi in sorted_x]

    first_lo, first_hi = intervals[0]
    span0 = first_hi - first_lo
    cost_at_low = abs(first_hi - ay) + span0
    cost_at_high = abs(first_lo - ay) + span0
    prev_lo, prev_hi = first_lo, first_hi

    for i in range(1, len(intervals)):
        cur_lo, cur_hi = intervals[i]
        span = cur_hi - cur_lo

        new_cost_at_low = min(cost_at_low + abs(cur_hi - prev_lo), cost_at_high + abs(cur_hi - prev_hi)) + span
        new_cost_at_high = min(cost_at_low + abs(cur_lo - prev_lo), cost_at_high + abs(cur_lo - prev_hi)) + span

        cost_at_low = new_cost_at_low
        cost_at_high = new_cost_at_high
        prev_lo, prev_hi = cur_lo, cur_hi

    final_cost = min(cost_at_low + abs(by - prev_lo), cost_at_high + abs(by - prev_hi))

    horizontal_cost = bx - ax
    print(horizontal_cost + final_cost)
