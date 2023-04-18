n = int(input())
line = list(map(int,input().split()))

best = line[0]
worst = line[0]
c = 0

for i in line:
    if i > best:
        best = i
        c += 1
    if i < worst:
        worst = i
        c+=1

print(c)
    



