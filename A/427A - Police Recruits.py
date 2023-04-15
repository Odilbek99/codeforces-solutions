n = int(input())
line = list(map(int,input().split()))

p_count = 0
c_count = 0

for el in line:
    if el == -1:
        if p_count > 0:
            p_count -= 1
        else:
            c_count +=1
    else:
        p_count += el

print(c_count)