n = int(input())
c = 0
for i in range(n):
    line = list(map(int, input().split()))
    if line.count(1) > 1:
        c+=1
print(c)