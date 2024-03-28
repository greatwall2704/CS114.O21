from math import sqrt
n = int(input())

count = 0
for a in range(1, int(n/sqrt(2))):
    b = sqrt(n*n - a*a)
    if b.is_integer():
        count+=1
print(count)