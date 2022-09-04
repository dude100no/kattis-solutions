import math
import time

n = int(input())

start_time = time.time()

ans = n
for i in range(1, n):
	days_for_printer = math.ceil(math.log(i, 2))
	filler = (2 ** days_for_printer) - i
	remaining_days = math.ceil((n - filler) / i)
	ans = min(ans, remaining_days + days_for_printer)

print(ans)
print(time.time() - start_time)