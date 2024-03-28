n = int(input())
x = []
y = []
vector = []
for _ in range(n):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)
for i in range(1, n):
    a, b = x[i] - x[i-1], y[i] - y[i-1]
    vector.append([a,b,x[i],y[i]])
count = 0
for i in range(n-2):
    if vector[i][0] * vector[i+1][0] + vector[i][1] * vector[i+1][1] == 0:
        if vector[i][1] > 0 and vector[i][2] < vector[i+1][2]:
            count += 1
        elif vector[i][1] < 0 and vector[i][2] > vector[i+1][2]:
            count += 1
        elif vector[i][1] == 0:
            if vector[i][0] > 0 and vector[i][3] > vector[i+1][3]:
                count += 1
            elif vector[i][0] < 0 and vector[i][3] < vector[i+1][3]:
                count += 1

print(count)
