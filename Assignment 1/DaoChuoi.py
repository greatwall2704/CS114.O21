def can_transform(a, b):
    if len(a) != len(b):
        return False
    else:
        if a == b:
            return True
        a_even = ""
        a_odd = ""
        b_even = ""
        b_odd = ""
        for i in range(1, len(a), 2):
            a_even = a_even + a[i]
        for i in range(0, len(a), 2):
            a_odd = a_odd + a[i]
        for i in range(1, len(a), 2):
            b_even = b_even + b[i]
        for i in range(0, len(a), 2):
            b_odd = b_odd + b[i]
        a_even = ''.join(sorted(a_even))
        b_even = ''.join(sorted(b_even))
        a_odd = ''.join(sorted(a_odd))   
        b_odd = ''.join(sorted(b_odd))  
        if a_even == b_even and a_odd == b_odd:
            return True 

t = int(input())

for _ in range(t):
    a = input().strip()
    b = input().strip()
    
    if can_transform(a, b):
        print("YES")
    else:
        print("NO")