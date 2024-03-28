r, c = map(int,input().split())
row = []
for _ in range(r):
    x = input()
    row.append(x)
for i in range(r):
    print(row[r - i - 1])