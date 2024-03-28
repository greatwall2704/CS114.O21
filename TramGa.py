arr = []
count = 0

for i in range(2):
    row = input()
    for j in row:
        if j == '#':
            count = count + 1
    arr.append(row)

if count >= 3:
    print("Yes")
if count == 2:
    if (arr[0][0] == '#' and arr[1][1] == '#') or (arr[0][1] == '#' and arr[1][0] == '#'):
        print("No")
    else:
        print("Yes")
    