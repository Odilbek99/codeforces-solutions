n, top = map(int, input().split())
line = list(map(int,input().split()))
c = 0

for i in range(n):
    if line[i] == 0:
        break
    
    if i < top:
        c+=1
    else:
        if line[i] == line[i-1]:
            c += 1
        else:
            break

print(c)




