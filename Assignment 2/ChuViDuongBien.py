ans = 0
r, c = map(int, input().split())
matrix = []
for _ in range(r):
  row = input().split()
  matrix.append([int(x) for x in row])
for i in range(r):
  for j in range(c):
    if matrix[i][j] == 1:
      ans += 4
      for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c:
          if matrix[ni][nj] == 1:
            ans -= 1
print(ans)



