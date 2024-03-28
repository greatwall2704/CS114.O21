r, c = map(int,input().split())
matrix = []
for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)
ans = [[0 for _ in range(c)] for _ in range(r)]
if r == 1:
    for i in range(1, c):  
        ans[0][i] = matrix[0][i-1]
    ans[0][0] = matrix[0][c - 1]
elif c == 1:
    for i in range(1, r):
        ans[i][0] = matrix[i - 1][0]      
    ans[0][0] = matrix[r - 1][0]   
else: 
    x = min(r, c) // 2
    for k in range(x + 1):
        count_row = r - 2 * k
        count_col = c - 2 * k 
        row_top = k
        row_bottom = r - k - 1
        col_left = k 
        col_right = c - k - 1
        if k % 2 == 0:
            if count_row != 1 and count_col != 1:
                for i in range(col_left + 1, col_right + 1):  
                    ans[row_top][i] = matrix[row_top][i-1]
                
                for i in range(row_top + 1, row_bottom + 1):
                    ans[i][col_right] = matrix[i - 1][col_right]
                
                for i in range(col_right - 1, col_left - 1, -1):
                    ans[row_bottom][i] = matrix[row_bottom][i + 1]
                    
                for i in range(row_bottom - 1, row_top - 1, -1 ):
                    ans[i][col_left] = matrix[i + 1][col_left] 
            
            elif count_row == 1 and count_col > 1:
                for i in range(col_left + 1, col_right + 1):  
                    ans[row_top][i] = matrix[row_top][i-1]
                ans[row_top][col_left] = matrix[row_top][col_right]
                
            elif count_col == 1 and count_row > 1:
                for i in range(row_top + 1, row_bottom + 1):
                    ans[i][col_right] = matrix[i - 1][col_right]
                ans[row_top][col_right] = matrix[row_bottom][col_right]
                  
        
        else:
            if count_row != 1 and count_col != 1:
                for i in range(col_left + 1, col_right + 1):  
                    ans[row_bottom][i] = matrix[row_bottom][i-1]
                
                for i in range(row_top + 1, row_bottom + 1):
                    ans[i][col_left] = matrix[i - 1][col_left]
                
                for i in range(col_right - 1, col_left - 1, -1):
                    ans[row_top][i] = matrix[row_top][i + 1]
                    
                for i in range(row_bottom - 1, row_top - 1, -1 ):
                    ans[i][col_right] = matrix[i + 1][col_right]   
            
            elif count_row == 1 and count_col > 1:
                for i in range(col_right - 1, col_left - 1, -1):
                    ans[row_top][i] = matrix[row_top][i + 1]
                ans[row_top][col_right] = matrix[row_top][col_left]
                
            elif count_col == 1 and count_row > 1:
                for i in range(row_bottom - 1, row_top - 1, -1 ):
                    ans[i][col_right] = matrix[i + 1][col_right]  
                ans[row_bottom][col_right] = matrix[row_top][col_right]
        if count_col == 1 and count_row == 1:
                ans[k][k] = matrix[k][k]

for row in ans:
    print(" ".join(map(str, row)))