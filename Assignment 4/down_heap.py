import heapq
def request_1(arr):
    
arr = []
n = int(input())
for _ in range(n):
    x = int(input())
    arr.append(x*(-1))
heapq.heapify(arr)
print(arr)

