n = int(input())
thoi_gian = list(map(float, input().split()))
x = float(input())
y = float(input())
z = float(input())

tong_sat_thuong = 0
thoi_gian_gai_duy_tri = [0] * n
for i in range(n):
    thoi_gian_gai_duy_tri[i] = thoi_gian[i] + z
    
for i in range(n):
    tong_sat_thuong += x
    so_gai = 0
    j = i - 1
    while j >= 0 and thoi_gian_gai_duy_tri[j] >= thoi_gian[i]:
        so_gai += 1
        j -= 1
    tong_sat_thuong += so_gai * y
print(int(tong_sat_thuong))
    

