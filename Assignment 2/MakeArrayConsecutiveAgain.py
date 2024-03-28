n = int(input())
num_min = 1000000
num_max = -1000000
for _ in range(n):
    x = int(input())
    num_min = min(num_min, x)
    num_max = max(num_max, x)
ans = num_max - num_min + 1 - n
print(ans)