t = int(input())
for _ in range(t):
	n = int(input())
	tasks = [tuple(map(int, input().split())) for _ in range(n)]
	best = 0
	for c, p in reversed(tasks):
		q = 1.0 - p / 100.0
		take = c + q * best
		if take > best:
			best = take
	print(f"{best:.10f}")
