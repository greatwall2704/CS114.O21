def Ktra_SNT(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def Tao_Mang_SNT(n):
  Mang_SNT = []
  for i in range(n):
      if Ktra_SNT(i):
          Mang_SNT.append(i)
  return Mang_SNT

def PhanTichThuaSNT(n, DS_SNT):
    i = 0
    factors = []
    while DS_SNT[i]**2 <= n:
        if n % DS_SNT[i] !=0:
            i += 1
        else:
            n //= DS_SNT[i]
            factors.append(DS_SNT[i])
    if n > 1:
        factors.append(n)
    return factors
  
from math import sqrt
arr = []
count = 0
L, R = map(int, input().split())
DS_SNT = Tao_Mang_SNT(int(sqrt(R))+30)
print(DS_SNT)
for i in range (L, R+1):
    tmp = PhanTichThuaSNT(i, DS_SNT)
    tmps = set(tmp)
    if len(tmp) == len(tmps):
        arr.append(tmps)

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if len(arr[i].intersection(arr[j])) == 0:
            count += 1
print(count)