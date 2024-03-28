import sys
def Tim_Dau_Cuoi(arr,k,x):
    left, right = 0, len(arr) - k
    while left < right:
        mid = left + (right - left) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    print(arr[left],arr[left + k - 1])
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    while True:
        try:
            k, x = map(int, sys.stdin.readline().strip().split())
            Tim_Dau_Cuoi(arr,k,x)
        except:
            break



