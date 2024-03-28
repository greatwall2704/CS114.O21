xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
A = (xA, yA)
B = (xB, yB)

AB = (xB - xA, yB - yA) 

AD1 = (-AB[1], AB[0])
xC1, yC1 = xB + AD1[0], yB + AD1[1]
xD1, yD1 = xA + AD1[0], yA + AD1[1]
C1 = (xC1, yC1) 
D1 = (xD1, yD1)

AD2 = (AB[1], -AB[0])
xC2, yC2 = xB + AD2[0], yB + AD2[1]
xD2, yD2 = xA + AD2[0], yA + AD2[1]
C2 = (xC2, yC2) 
D2 = (xD2, yD2)
print(A,D1,C1,B)
print(A,B,C2,D2)
    