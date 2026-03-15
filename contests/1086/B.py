t = int(input())
for _ in range(t):
	n, k, p, m = map(int, input().split())
	cards = list(map(int, input().split()))
	win = cards[p - 1]
	if win > m:
		print(0)
		continue
	prefix_cost = 0
	if p > k:
		need = p - k
		prefix = cards[: p - 1]
		prefix.sort()
		prefix_cost = sum(prefix[:need])
	first_cost = prefix_cost + win
	if first_cost > m:
		print(0)
		continue
	others = cards[: p - 1] + cards[p:]
	others.sort()
	filler_cnt = n - k
	filler_sum = sum(others[:filler_cnt]) if filler_cnt > 0 else 0
	cycle_cost = win + filler_sum
	answer = 1 + (m - first_cost) // cycle_cost
	print(answer)
