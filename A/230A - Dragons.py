s,n = map(int,input().split())
c = s
t = []
res = None
for i in range(n):
    x,y = map(int,input().split())
    t.append((x,y))
    
t = sorted(t, key=lambda x: (x[0],-x[1]))
for i in t:
       
    if c > i[0]:
        c+=i[1]
        res = 'YES'
    else:
        res = 'NO'
print(res)
