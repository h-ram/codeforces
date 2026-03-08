def best_oneside(array, h):
	n = len(array)
	best = [0] * (n + 1)
	for drain in range(n):
		current = 0
		highest = 0

		for left in range(drain, -1, -1):
			highest = max(highest, array[left])
			current += h - highest

		best[drain + 1] = max(best[drain + 1], current)
		highest = array[drain]
		for right in range(drain + 1, n):
			highest = max(highest, array[right])
			current += h - highest
			best[right + 1] = max(best[right + 1], current)

	return best

t = int(input())
for _ in range(t):
	n, h = map(int, input().split())
	a = list(map(int, input().split()))

	prefix = best_oneside(a, h)
	suffix_reversed = best_oneside(a[::-1], h)
	answer = 0
	for split in range(n + 1):
		left = prefix[split]
		right = suffix_reversed[n - split]
		answer = max(answer, left + right)

	print(answer)

