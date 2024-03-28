def generate_combinations(n, k):
  combinations = []
  indices = []
  # Duyệt qua từng tổ hợp
  def backtrack(i, j, curr_combination):
    if j == k:
      # Thêm tổ hợp và chỉ số vào danh sách
      combinations.append(curr_combination)
      indices.append(list(curr_combination))
      return

    # Duyệt qua các phần tử còn lại
    for l in range(i + 1, n + 1):
      backtrack(l, j + 1, curr_combination + [l])

  backtrack(0, 0, [])

  return combinations, indices
h, w, k = map(int, input().split())
matrix = []
for _ in range(h):
  row = list(input())
  matrix.append(row)
sum = 0
ans = 0    
count_row = [0] * h
count_col = [0] * w

for i in range(h):
  for j in range(w):
      if matrix[i][j] == "#":
          sum += 1
          count_row[i] += 1
          count_col[j] += 1      
if sum == k:
  ans += 1
for r in range(1, h + 1):
  combinations_row, indices_row = generate_combinations(h, r)
  for index_row in indices_row:
    count = 0
    for m in range(r):
      count += count_row[index_row[m] - 1]
    if sum - count == k:
      ans += 1

      
for c in range(1, w + 1):
  combinations_col, indices_col = generate_combinations(w, c)
  for index_col in indices_col:
    count = 0
    for n in range(c):
      count += count_col[index_col[n] - 1]
    if sum - count == k:
      ans += 1
    
for r in range(1, h + 1):
  combinations_row, indices_row = generate_combinations(h, r)
  for index_row in indices_row:
    count = 0
    for m in range(r):
      count += count_row[index_row[m] - 1]
    for c in range(1, w + 1):
      combinations_col, indices_col = generate_combinations(w, c)
      for index_col in indices_col:
        x = count
        for n in range(c):
          x += count_col[index_col[n] - 1]
          for m in range(r):
            if matrix[index_row[m] - 1][index_col[n] - 1] == "#":
              x -= 1 
        if sum - x == k:
          ans += 1
   
print(ans)


