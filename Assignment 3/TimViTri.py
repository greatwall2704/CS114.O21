def binary_search(array, x):
  low = 0
  high = len(array) - 1
  result = -1

  while low <= high:
    mid = (low + high) // 2
    if array[mid] == x:
      result = mid
      low = mid + 1
    elif array[mid] < x:
      low = mid + 1
    else:
      high = mid - 1

  return result

n = int(input())
a = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
for i in range(m):
    result = binary_search(a, x[i])
    print(result)