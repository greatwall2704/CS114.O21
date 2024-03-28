def count_trip(matrix, x):
    count = 0
    sum = 0
    for i in range(len(matrix) - 1):
        sum += matrix[i]
        if sum + matrix[i+1] > x:
            sum = 0
            count += 1
    count += 1
    return count
l, m = map(int, input().split())
cars = []
for _ in range(m):
    length, position = input().split()
    cars.append((int(length), position))
left = []
right = []
ans = 0
for i in range(m):
    if cars[i][1] == "left":
        left.append(cars[i][0])
    else:
        right.append(cars[i][0])
if count_trip(left, l * 100) > count_trip(right, l * 100):
    ans = 2 * count_trip(right, l * 100) + 2 * (count_trip(left, l * 100) - count_trip(right, l * 100)) - 1
else:
    ans = 2 * count_trip(left, l * 100) + 2 * (count_trip(right, l * 100) - count_trip(left, l * 100))
print(ans)
    