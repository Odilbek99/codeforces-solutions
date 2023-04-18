n,k = map(int,input().split())
res = 0
c=0
minute = 240 - k
for i in range(1,n+1):
    if res+5*i <= minute:
        c += 1
        res += 5*i

    else:
        break

print(c)