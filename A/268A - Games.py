n = int(input())
d = {}
d1 = {}
for i in range(n):
    a,b = map(int,input().split())

    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

    if b not in d1:
        d1[b] = 1
    else:
        d1[b] +=1 
c = 0
intersect = d.keys() & d1.keys()
for i in intersect:
    c += d[i]*d1[i]
print(c)

# print(d)