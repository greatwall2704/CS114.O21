def check_transferable(array):
  n = len(array)
  mid = n // 2 if n % 2 == 1 else n // 2 - 1

  unequal_count = 0
  for i in range(mid + 1):
    if array[i] != array[n - i - 1]:
      unequal_count += 1

  return unequal_count <= 1

import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
  array.append(int(sys.stdin.readline()))

if check_transferable(array):
  print("TRUE")
else:
  print("FALSE")
