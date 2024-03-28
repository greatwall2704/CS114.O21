def count_regions(matrix):
  m, n = len(matrix), len(matrix[0])
  visited = [[False for _ in range(n)] for _ in range(m)]
  count = 0
  for i in range(m):
    for j in range(n):
      if not visited[i][j] and matrix[i][j] == '-':
        count += 1
        _dfs(matrix, visited, i, j)
  return count

def _dfs(matrix, visited, i, j):
  m, n = len(matrix), len(matrix[0])
  visited[i][j] = True
  for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    ni, nj = i + di, j + dj
    if 0 <= ni < m and 0 <= nj < n:
      if not visited[ni][nj] and matrix[ni][nj] == '-':
        _dfs(matrix, visited, ni, nj)
a = 0
while True:
  try:
    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(input()))  
    count = count_regions(matrix)
    print(f"Case {a+1}: {count}",)
    a+=1
  except:
    break



